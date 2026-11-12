"""Extract archived official curriculum HTML. Requires lxml; performs no network access."""

import hashlib
import json
import re
from pathlib import Path

from lxml import html


ROOT = Path(__file__).resolve().parents[1] / "references" / "curricula"
SOURCES = [
    ("P01", "3261", "统计学", "public_summary"),
    ("P02", "3263", "应用统计学", "public_summary"),
    ("P03", "3260", "数据科学", "public_summary"),
    ("P04", "3258", "经济统计学", "public_summary"),
    ("P05", "3259", "经济统计学（经济数据工程实验班）", "public_summary"),
    ("P06", "4845", "数学与应用数学（保险精算方向）", "historical_summary"),
    ("H01", "1489", "统计学", "historical_summary"),
    ("H02", "1490", "应用统计学", "historical_summary"),
    ("H03", "1491", "应用统计学", "historical_summary"),
    ("H04", "1487", "经济统计学", "historical_summary"),
    ("H05", "1488", "经济统计学（经济数据工程实验班）", "historical_summary"),
]
SUPPLEMENTAL = {
    "index": "https://tjysjkx.jlufe.edu.cn/rcpy/bkspy/pyfa.htm",
    "index-older": "https://tjysjkx.jlufe.edu.cn/rcpy/bkspy/pyfa/1.htm",
    "legacy-3261": "https://newtjxy.jlufe.edu.cn/info/1084/3261.htm",
    "school-admissions-2024": "https://www.jlufe.edu.cn/info/1045/14483.htm",
    "school-credit-rule": "https://jwc.jlufe.edu.cn/info/1156/1909.htm",
    "school-course-plan-2026": "https://jwc.jlufe.edu.cn/info/1032/2316.htm",
    "experimental-selection-2025": "https://newtjxy.jlufe.edu.cn/info/1117/3927.htm",
}


def clean(text):
    return re.sub(r"\s+", " ", text).strip()


def archive_record(path, url):
    content = path.read_bytes()
    return {
        "url": url,
        "downloaded_on": "2026-11-10",
        "retrieval_status": "complete_html_archive",
        "local_file": path.relative_to(ROOT).as_posix(),
        "bytes": len(content),
        "sha256": hashlib.sha256(content).hexdigest(),
    }


def extract(source_id, page_id, programme, role):
    path = ROOT / "pages" / f"{page_id}.html"
    url = f"https://tjysjkx.jlufe.edu.cn/info/1084/{page_id}.htm"
    tree = html.fromstring(path.read_bytes())
    bodies = tree.xpath('//*[contains(concat(" ",normalize-space(@class)," "), " v_news_content ")]')
    if len(bodies) != 1:
        raise ValueError(f"{source_id}: expected one article body, got {len(bodies)}")
    body = bodies[0]
    paragraphs = [clean(p.text_content()) for p in body.xpath('.//p[not(ancestor::table)]')]
    paragraphs = [p for p in paragraphs if p]
    if not paragraphs:
        paragraphs = [clean(body.text_content())]
    title = clean(tree.xpath("string(//title)"))
    published = re.search(r"发布时间\s*[：:]\s*(\d{4}-\d{2}-\d{2})", tree.text_content())
    attachment_labels = [p for p in paragraphs if re.match(r"附件\d+[：:]", p)]
    label_years = sorted({int(y) for p in attachment_labels for y in re.findall(r"(20\d{2})级", p)})
    match = re.search(r"本专业主要课程包括[：:](.+?)(?:。|$)", clean(body.text_content()))
    if match is None:
        raise ValueError(f"{source_id}: main-course paragraph missing")
    course_names = [name.strip().removesuffix("等") for name in match.group(1).split("、")]
    courses = [{
        "name": name,
        "credits": None,
        "course_code": None,
        "course_type": None,
        "semester": None,
        "syllabus_details": None,
        "eligible_for_recommendation_average": None,
        "evidence_location": "主要课程段落",
        "evidence_status": "name_only_in_official_overview",
    } for name in course_names]

    tables = []
    modules = []
    for table in body.xpath('.//table[not(ancestor::table)]'):
        rows = [[clean(cell.text_content()) for cell in row.xpath('./th|./td')]
                for row in table.xpath('./tr|./tbody/tr|./thead/tr')]
        tables.append(rows)
        labels = next((row[1:] for row in rows if row and row[0] == "模块设置"), None)
        values = next((row[1:] for row in rows if row and row[0] in ("学分", "学分要求")), None)
        if labels is not None and values is not None:
            if len(labels) != len(values):
                raise ValueError(f"{source_id}: unmatched module labels and credits")
            modules = [{"name": name, "credits": float(value)} for name, value in zip(labels, values)]
    totals = re.search(r"理论教学\s*(\d+)\s*学分，实践教学\s*(\d+)\s*学分，合计\s*(\d+)\s*学分", body.text_content())
    summary = None
    if totals:
        theory, practice, total = map(int, totals.groups())
        if theory + practice != total or sum(m["credits"] for m in modules) != total:
            raise ValueError(f"{source_id}: module and graduation totals disagree")
        summary = {"theory": theory, "practice": practice, "total": total, "basis": "stated_in_article"}
    elif modules:
        theory_match = re.search(r"理论教学含必修课和选修课共计\s*(\d+)\s*学分", body.text_content())
        practice_match = re.search(r"实践教学共计\s*(\d+)\s*学分", body.text_content())
        theory = int(theory_match.group(1)) if theory_match else None
        practice = int(practice_match.group(1)) if practice_match else None
        total = sum(m["credits"] for m in modules)
        if theory is not None and practice is not None and theory + practice != total:
            raise ValueError(f"{source_id}: narrative credits and module totals disagree")
        summary = {"theory": theory, "practice": practice, "total": total,
                   "basis": "sum_of_stated_modules"}

    text_path = ROOT / "extracted" / f"{source_id}.txt"
    output = [title, url, "下载日期 2026-11-10", "", "正文段落"]
    output.extend(f"[P{n:03d}] {p}" for n, p in enumerate(paragraphs, 1))
    output.append("\n原文表格（各行保留原单元格顺序）")
    for table_number, table in enumerate(tables, 1):
        output.extend(f"[T{table_number:02d}-R{n:02d}] " + " | ".join(row) for n, row in enumerate(table, 1))
    text_path.write_text("\n".join(output) + "\n", encoding="utf-8")
    return {
        "source_id": source_id,
        "programme": programme,
        "role": role,
        "published_on": published.group(1) if published else None,
        "source": archive_record(path, url),
        "extracted_file": text_path.relative_to(ROOT).as_posix(),
        "article_text_sha256": hashlib.sha256(body.text_content().encode("utf-8")).hexdigest(),
        "cohorts_named_in_attachment_labels": label_years,
        "cohort_applicability_verified_from_course_table": False,
        "cohort_evidence_note": "附件标题年级仅为定位线索；发布日期不代表入学年级；逐课表未取得，其他年级适用性未知。",
        "attachment_labels": attachment_labels,
        "article_link_targets": body.xpath('.//a/@href'),
        "article_embedded_sources": body.xpath('.//img/@src|.//iframe/@src|.//embed/@src|.//object/@data'),
        "graduation_credits": summary,
        "module_credits": modules,
        "main_courses": courses,
        "full_course_list_obtained": False,
        "per_course_credits_obtained": False,
    }


def main():
    (ROOT / "extracted").mkdir(exist_ok=True)
    plans = [extract(*source) for source in SOURCES]
    supplemental = []
    for key, url in SUPPLEMENTAL.items():
        path = ROOT / "pages" / f"{key}.html"
        if path.exists():
            supplemental.append(archive_record(path, url))
        else:
            supplemental.append({"url": url, "local_file": None,
                                 "retrieval_status": "html_download_failed_or_incomplete",
                                 "checked_on": "2026-11-10"})
    data = {
        "schema_version": "1.0",
        "checked_on": "2026-11-10",
        "scope": "吉林财经大学统计与数据科学学院各年级；年级适用性逐项核实",
        "unknown_value": "null means unavailable or unverified, never zero credits",
        "plans": plans,
        "supplemental_sources": supplemental,
        "missing_programmes": [{"programme": "金融数学", "status": "no_verified_public_curriculum_found"}],
    }
    (ROOT / "catalog.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    primary = [p for p in plans if p["source_id"].startswith("P")]
    print(json.dumps({
        "archived_sources": len(plans) + sum(s["local_file"] is not None for s in supplemental),
        "curriculum_articles": len(plans),
        "primary_course_mentions": sum(len(p["main_courses"]) for p in primary),
        "verified_per_course_credits": 0,
        "programmes": [{"source_id": p["source_id"], "programme": p["programme"],
                        "published_on": p["published_on"], "courses": len(p["main_courses"]),
                        "graduation_credits": p["graduation_credits"]} for p in primary],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
