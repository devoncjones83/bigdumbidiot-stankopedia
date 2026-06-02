#!/usr/bin/env python3
import subprocess
from datetime import datetime, timezone

DB_CONTAINER="wikijs-postgres"
DB_USER="wikijs"
DB_NAME="wikijs"

CATEGORIES = {
  "stankopedia/agencies": "Agencies and Organizations",
  "stankopedia/doctrine": "Doctrine",
  "stankopedia/food": "Snack Studies",
  "stankopedia/government": "Government Documents",
  "stankopedia/history": "Historical Records",
  "stankopedia/lore": "Lore and Forbidden Knowledge",
  "stankopedia/people": "Important Figures",
  "stankopedia/science": "Scientific Research",
  "stankopedia/standards": "Standards and Procedures",
  "stankopedia/technology": "Technology and Digital Stank",
}

def q(s):
    return "'" + s.replace("'", "''") + "'"

sql = ["BEGIN;"]

for path, title in CATEGORIES.items():
    content = f"""# {title}

Welcome to the **{title}** section of Stankopedia.

This category contains certified nonsense, questionable research, and dangerous levels of institutional funk.

[Return to Stankopedia Home](/stankopedia/home)
"""
    render = f"""<h1>{title}</h1>
<p>Welcome to the <strong>{title}</strong> section of Stankopedia.</p>
<p>This category contains certified nonsense, questionable research, and dangerous levels of institutional funk.</p>
<p><a href="/stankopedia/home">Return to Stankopedia Home</a></p>
"""
    sql.append(f"""
UPDATE pages
SET content = {q(content)},
    render = {q(render)},
    "updatedAt" = now()::text
WHERE path = {q(path)};
""")

sql.append("COMMIT;")

p = subprocess.run(
    ["docker","exec","-i",DB_CONTAINER,"psql","-U",DB_USER,"-d",DB_NAME],
    input="\n".join(sql),
    text=True
)

raise SystemExit(p.returncode)
