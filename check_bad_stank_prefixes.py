#!/usr/bin/env python3
import re
import subprocess

DB_CONTAINER="wikijs-postgres"
DB_USER="wikijs"
DB_NAME="wikijs"

BAD_PREFIXES = (
    "/people/",
    "/history/",
    "/science/",
    "/standards/",
    "/food/",
    "/government/",
    "/agencies/",
    "/doctrine/",
    "/lore/",
    "/technology/",
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
SELECT id, path, content
FROM pages
WHERE path LIKE 'stankopedia/%' OR path='home';
""").splitlines()

bad=[]

for row in rows:
    parts=row.split("\t",2)
    if len(parts) != 3:
        continue

    page_id, source, content = parts
    for label,target in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content):
        if target.startswith(BAD_PREFIXES):
            bad.append((page_id, source, label, target))

if not bad:
    print("No bad stank prefixes found.")
else:
    print(f"Bad stank prefixes found: {len(bad)}\n")
    for page_id, source, label, target in bad:
        print(f"ID {page_id} | {source}")
        print(f"  {label} -> {target}")
        print()
