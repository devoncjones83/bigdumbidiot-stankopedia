#!/usr/bin/env python3
import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

PAGES_DIR = Path("/mnt/user/appdata/bigdumbidiot-stankopedia/pages")
ROOT_PATH = "stankopedia"
DB_CONTAINER = "wikijs-postgres"
DB_USER = "wikijs"
DB_NAME = "wikijs"
AUTHOR_ID = 1
LOCALE = "en"

def now():
    return datetime.now(timezone.utc).isoformat()

def title_from_filename(path):
    return path.stem.replace("-", " ").title()

def strip_frontmatter(text):
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return parts[2].lstrip()
    return text

def page_path(md):
    rel = md.relative_to(PAGES_DIR).with_suffix("")
    parts = list(rel.parts)
    return "/".join([ROOT_PATH] + parts)

def sql_quote(value):
    if value is None:
        return "NULL"
    return "'" + str(value).replace("'", "''") + "'"

def run_sql(sql):
    p = subprocess.run(
        ["docker", "exec", "-i", DB_CONTAINER, "psql", "-U", DB_USER, "-d", DB_NAME],
        input=sql,
        text=True,
        capture_output=True
    )
    if p.returncode != 0:
        print(p.stderr)
        raise SystemExit(p.returncode)
    return p.stdout

def main():
    files = sorted(PAGES_DIR.rglob("*.md"))
    files = [f for f in files if not f.name.endswith(".disabled")]

    ts = now()

    sql = ["BEGIN;"]

    sql.append("""
INSERT INTO tags (tag, title, "createdAt", "updatedAt")
VALUES ('stankopedia', 'Stankopedia', {ts}, {ts})
ON CONFLICT (tag) DO NOTHING;
""".format(ts=sql_quote(ts)))

    for md in files:
        raw = md.read_text(encoding="utf-8")
        content = strip_frontmatter(raw)
        path = page_path(md)
        title = title_from_filename(md)
        description = "A Big Dumb Idiot Labs Stankopedia page."
        h = hashlib.sha1(path.encode("utf-8")).hexdigest()
        page_ts = now()

        sql.append(f"""
INSERT INTO pages (
  path, hash, title, description, "isPrivate", "isPublished",
  "privateNS", "publishStartDate", "publishEndDate",
  content, render, toc, "contentType",
  "createdAt", "updatedAt", "editorKey", "localeCode",
  "authorId", "creatorId", extra
)
VALUES (
  {sql_quote(path)}, {sql_quote(h)}, {sql_quote(title)}, {sql_quote(description)},
  false, true,
  NULL, NULL, NULL,
  {sql_quote(content)}, {sql_quote(content)}, '[]'::json, 'markdown',
  {sql_quote(page_ts)}, {sql_quote(page_ts)}, 'markdown', {sql_quote(LOCALE)},
  {AUTHOR_ID}, {AUTHOR_ID}, '{{}}'::json
)
ON CONFLICT DO NOTHING;
""")

        sql.append(f"""
INSERT INTO "pageTags" ("pageId", "tagId")
SELECT p.id, t.id
FROM pages p, tags t
WHERE p.path = {sql_quote(path)}
AND t.tag = 'stankopedia'
AND NOT EXISTS (
  SELECT 1 FROM "pageTags" pt WHERE pt."pageId" = p.id AND pt."tagId" = t.id
);
""")

    sql.append("COMMIT;")
    run_sql("\n".join(sql))
    print(f"Imported/checked {len(files)} stank pages.")

if __name__ == "__main__":
    main()
