"""Recalculate first-attempt course averages for an explicitly selected scope."""

import argparse
import json
import sys
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP, localcontext
from pathlib import Path


def number(value, field):
    if isinstance(value, bool) or not isinstance(value, (str, int, float, Decimal)):
        raise ValueError(f"{field} must be a number")
    try:
        result = Decimal(str(value))
    except InvalidOperation as exc:
        raise ValueError(f"{field} must be a number") from exc
    if not result.is_finite():
        raise ValueError(f"{field} must be finite")
    return result


def calculate(data):
    if not isinstance(data, dict):
        raise ValueError("Input must be a JSON object")
    if data.get("scope_confirmed") is not True:
        raise ValueError("Confirm the applicable course scope before calculation")
    source = data.get("scope_source")
    if not isinstance(source, str) or not source.strip():
        raise ValueError("scope_source is required")
    courses = data.get("courses")
    if not isinstance(courses, list) or not courses:
        raise ValueError("courses must be a nonempty list")

    seen = set()
    included = []
    excluded = []
    below_60 = []
    unknown_required = []
    credits_total = Decimal(0)
    points_total = Decimal(0)

    with localcontext() as context:
        context.prec = 40
        for course in courses:
            if not isinstance(course, dict):
                raise ValueError("Each course must be an object")
            course_id = course.get("course_id")
            if not isinstance(course_id, str) or not course_id.strip():
                raise ValueError("Every course needs a course_id")
            course_id = course_id.strip()
            if course_id in seen:
                raise ValueError(f"Duplicate course_id: {course_id}")
            seen.add(course_id)
            required = course.get("required")
            include = course.get("include_in_average")
            if type(required) is not bool or type(include) is not bool:
                raise ValueError(f"{course_id}: required and include_in_average must be booleans")
            if include and not required:
                raise ValueError(f"{course_id}: selected courses must be required courses")
            credits = number(course.get("credits"), f"{course_id}.credits")
            if credits < 0:
                raise ValueError(f"{course_id}: credits cannot be negative")
            score = course.get("initial_score")
            if score is not None:
                score = number(score, f"{course_id}.initial_score")
                if not Decimal(0) <= score <= Decimal(100):
                    raise ValueError(f"{course_id}: initial_score must be within 0 to 100")
            if required and score is None:
                unknown_required.append(course_id)
            if required and score is not None and score < 60:
                below_60.append(course_id)
            if include:
                if score is None:
                    raise ValueError(f"{course_id}: an included course needs its initial score")
                included.append(course_id)
                credits_total += credits
                points_total += credits * score
            else:
                excluded.append(course_id)

        if credits_total <= 0:
            raise ValueError("The included courses must have positive total credits")
        average = points_total / credits_total
        return {
            "scope_source": source,
            "included_course_ids": included,
            "excluded_course_ids": excluded,
            "total_credits": str(credits_total),
            "weighted_points": str(points_total),
            "average_decimal": str(average),
            "average_display_4dp": str(average.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)),
            "required_course_scores_below_60": below_60,
            "required_courses_with_unknown_initial_score": unknown_required,
            "interpretation": "Recalculation of supplied first-attempt records. Course scope, transcript completeness, ranking and eligibility require separate verification.",
        }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="UTF-8 JSON course records")
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8-sig"), parse_float=Decimal)
        result = calculate(data)
    except (OSError, UnicodeError, ValueError, InvalidOperation) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
