#!/usr/bin/env python3
import hashlib
import json
import posixpath
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import markdown

ROOT = Path("/mnt/user/appdata/bigdumbidiot-stankopedia")
PAGES_DIR = ROOT / "pages"
DB_CONTAINER = "wikijs-postgres"
DB_USER = "wikijs"
DB_NAME = "wikijs"
LOCALE = "en"
AUTHOR_ID = 1
ROOT_PATH = "stankopedia"

def now():
    return datetime.now(timezone.utc).isoformat()

def q(value):
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

def strip_frontmatter(text):
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return parts[2].lstrip()
    return text

def title_from_md(md):
    text = md.read_text(encoding="utf-8")
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if m:
        return m.group(1).strip().replace("🦨 ", "").replace("☢️ ", "")
    return md.stem.replace("-", " ").title()

def page_path(md):
    rel = md.relative_to(PAGES_DIR).with_suffix("")
    return "/".join([ROOT_PATH] + list(rel.parts))

def fix_links(content, current_path):
    current_dir = posixpath.dirname(current_path)

    def repl(match):
        label = match.group(1)
        target = match.group(2)

        if target.startswith(("http://", "https://", "mailto:", "#")):
            return match.group(0)

        if target.startswith("/en/"):
            fixed = target
        elif target.startswith("/stankopedia/"):
            fixed = "/en" + target
        elif target.startswith("../") or target.startswith("./"):
            normalized = posixpath.normpath(posixpath.join(current_dir, target))
            fixed = "/en/" + normalized
        elif target.startswith("/"):
            fixed = target
        else:
            normalized = posixpath.normpath(posixpath.join(current_dir, target))
            fixed = "/en/" + normalized

        fixed = fixed.replace("/en/stankopedia//", "/en/stankopedia/")
        return f"[{label}]({fixed})"

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl, content)

sql = ["BEGIN;"]

for md in sorted(PAGES_DIR.rglob("*.md")):
    if md.name.endswith(".disabled"):
        continue

    raw = md.read_text(encoding="utf-8")
    content = strip_frontmatter(raw)
    path = page_path(md)
    content = fix_links(content, path)
    rendered = markdown.markdown(content, extensions=["extra", "tables", "sane_lists"])
    title = title_from_md(md)
    ts = now()
    h = hashlib.sha1(path.encode("utf-8")).hexdigest()

    sql.append(f"""
UPDATE pages
SET content = {q(content)},
    render = {q(rendered)},
    toc = '[]'::json,
    hash = {q(h)},
    title = {q(title)},
    "publishStartDate" = '',
    "publishEndDate" = '',
    "contentType" = 'markdown',
    "editorKey" = 'markdown',
    "localeCode" = {q(LOCALE)},
    "authorId" = {AUTHOR_ID},
    "creatorId" = {AUTHOR_ID},
    "updatedAt" = {q(ts)}
WHERE path = {q(path)};
""")

sql.append("COMMIT;")
run_sql("\n".join(sql))
print("Restored clean stank from source Markdown files.")
