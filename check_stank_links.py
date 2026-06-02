#!/usr/bin/env python3
import re
import subprocess

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

rows=run_sql("""
SELECT path, content
FROM pages
WHERE path LIKE 'stankopedia/%' OR path='home';
""").splitlines()

existing=set()
for line in run_sql("SELECT path FROM pages;").splitlines():
    existing.add(line.strip())

bad=[]

for row in rows:
    if "\t" not in row:
        continue
    source, content = row.split("\t", 1)

    links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content)
    for label, target in links:
        if target.startswith(("http://","https://","mailto:","#")):
            continue

        clean = target.strip()
        clean = re.sub(r"^/+", "", clean)
        clean = re.sub(r"^en/", "", clean)
        clean = clean.split("#",1)[0].strip("/")

        if not clean:
            continue

        if clean not in existing:
            bad.append((source,label,target,clean))

if not bad:
    print("No broken stank links found.")
else:
    print(f"Broken stank links found: {len(bad)}\n")
    for source,label,target,clean in bad:
        print(f"SOURCE: {source}")
        print(f"  LINK: {label}")
        print(f"  TARGET: {target}")
        print(f"  EXPECTED PATH: {clean}")
        print()
