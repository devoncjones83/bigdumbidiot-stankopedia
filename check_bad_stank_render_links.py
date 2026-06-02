#!/usr/bin/env python3
import re
import subprocess

DB_CONTAINER="wikijs-postgres"
DB_USER="wikijs"
DB_NAME="wikijs"

BAD_PREFIXES = (
    "/people/", "/history/", "/science/", "/standards/", "/food/",
    "/government/", "/agencies/", "/doctrine/", "/lore/", "/technology/"
)

def run_sql(sql):
    p=subprocess.run(
        ["docker","exec","-i",DB_CONTAINER,"psql","-U",DB_USER,"-d",DB_NAME,"-t","-A","-F","\t"],
        input=sql,text=True,capture_output=True
    )
    if p.returncode != 0:
        print(p.stderr)
        raise SystemExit(p.returncode)
    return p.stdout

rows=run_sql("""
SELECT id, path, coalesce(content,''), coalesce(render,'')
FROM pages
WHERE path LIKE 'stankopedia/%' OR path='home';
""").splitlines()

bad=[]

for row in rows:
    parts=row.split("\t",3)
    if len(parts) != 4:
        continue
    page_id, source, content, render = parts

    for field_name, text in [("content", content), ("render", render)]:
        md_links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", text)
        html_links = re.findall(r'href="([^"]+)"', text)

        for label,target in md_links:
            if target.startswith(BAD_PREFIXES):
                bad.append((page_id, source, field_name, label, target))

        for target in html_links:
            if target.startswith(BAD_PREFIXES):
                bad.append((page_id, source, field_name, "HTML href", target))

if not bad:
    print("No bad stank prefixes found in content or render.")
else:
    print(f"Bad stank prefixes found: {len(bad)}\n")
    for page_id, source, field_name, label, target in bad:
        print(f"ID {page_id} | {source} | {field_name}")
        print(f"  {label} -> {target}")
        print()
