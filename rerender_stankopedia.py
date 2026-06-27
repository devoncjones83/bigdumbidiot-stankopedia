#!/usr/bin/env python3
import subprocess, html, json, markdown

DB_CONTAINER="wikijs-postgres"
DB_USER="wikijs"
DB_NAME="wikijs"

def run_sql(sql):
    p=subprocess.run(
        ["docker","exec","-i",DB_CONTAINER,"psql","-U",DB_USER,"-d",DB_NAME,"-t","-A","-F","\t"],
        input=sql,text=True,capture_output=True
    )
    if p.returncode != 0:
        print(p.stderr)
        raise SystemExit(p.returncode)
    return p.stdout

def q(s):
    if s is None:
        return "NULL"
    return "'" + s.replace("'","''") + "'"

rows=run_sql("""
SELECT id, content
FROM pages
WHERE path LIKE 'stankopedia/%';
""").splitlines()

updates=["BEGIN;"]

rendered_count = 0
skipped_count = 0

for row in rows:
    if not row.strip():
        skipped_count += 1
        continue

    if "\t" not in row:
        skipped_count += 1
        print(f"Skipping malformed row: {row[:120]!r}")
        continue

    page_id, content = row.split("\t", 1)
    rendered_count += 1

    rendered = markdown.markdown(
        content,
        extensions=["extra", "tables", "sane_lists"]
    )

    updates.append(f"""
UPDATE pages
SET render = {q(rendered)},
    toc = '[]'::json,
    "updatedAt" = now()::text
WHERE id = {int(page_id)};
""")

updates.append("COMMIT;")
run_sql("\n".join(updates))
print(f"Re-rendered {rendered_count} stank pages. Skipped {skipped_count} malformed/blank rows.")
