#!/usr/bin/env python3
import hashlib, subprocess
from datetime import datetime, timezone

DB_CONTAINER="wikijs-postgres"
DB_USER="wikijs"
DB_NAME="wikijs"

CATEGORIES = {
  "doctrine": "Doctrine",
  "government": "Government Documents",
  "science": "Scientific Research",
  "history": "Historical Records",
  "people": "Important Figures",
  "food": "Snack Studies",
  "agencies": "Agencies and Organizations",
  "lore": "Lore and Forbidden Knowledge",
  "standards": "Standards and Procedures",
  "technology": "Technology and Digital Stank",
}

def q(s):
    return "'" + str(s).replace("'", "''") + "'"

def run_sql(sql):
    p = subprocess.run(
        ["docker","exec","-i",DB_CONTAINER,"psql","-U",DB_USER,"-d",DB_NAME],
        input=sql,text=True,capture_output=True
    )
    if p.returncode != 0:
        print(p.stderr)
        raise SystemExit(p.returncode)

now = datetime.now(timezone.utc).isoformat()
sql = ["BEGIN;"]

for slug, title in CATEGORIES.items():
    path = f"stankopedia/{slug}"
    content = f"""# {title}

Welcome to the **{title}** section of Stankopedia.

This category contains certified nonsense, questionable research, and dangerous levels of institutional funk.

[Return to Stankopedia Home](/stankopedia/home)
"""
    h = hashlib.sha1(path.encode()).hexdigest()

    sql.append(f"""
INSERT INTO pages (
  path, hash, title, description, "isPrivate", "isPublished",
  "privateNS", "publishStartDate", "publishEndDate",
  content, render, toc, "contentType",
  "createdAt", "updatedAt", "editorKey", "localeCode",
  "authorId", "creatorId", extra
)
SELECT
  {q(path)}, {q(h)}, {q(title)}, 'Stankopedia category landing page.',
  false, true,
  NULL, '', '',
  {q(content)}, {q(content)}, '[]'::json, 'markdown',
  {q(now)}, {q(now)}, 'markdown', 'en',
  1, 1, '{{}}'::json
WHERE NOT EXISTS (
  SELECT 1 FROM pages WHERE path = {q(path)}
);
""")

sql.append("COMMIT;")
run_sql("\n".join(sql))
print("Created Stankopedia category landing pages.")
