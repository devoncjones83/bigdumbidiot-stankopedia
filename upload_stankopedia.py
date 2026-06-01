#!/usr/bin/env python3
"""
Big Dumb Idiot Labs - Stankopedia WikiJS Uploader
Uploads generated Markdown pages to WikiJS using GraphQL.

Requires:
  pip install requests python-dotenv pyyaml
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from typing import Dict, Tuple

import requests

try:
    import yaml
except ImportError:
    yaml = None

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None

ROOT = Path(__file__).resolve().parent
PAGES_DIR = ROOT / "pages"

if load_dotenv:
    load_dotenv(ROOT / ".env")

WIKIJS_URL = os.getenv("WIKIJS_URL", "").strip()
WIKIJS_TOKEN = os.getenv("WIKIJS_TOKEN", "").strip()
WIKIJS_LOCALE = os.getenv("WIKIJS_LOCALE", "en").strip()
WIKIJS_ROOT_PATH = os.getenv("WIKIJS_ROOT_PATH", "stankopedia").strip().strip("/")
DRY_RUN = os.getenv("DRY_RUN", "false").lower() in {"1", "true", "yes", "y"}

CREATE_MUTATION = """
mutation CreatePage(
  $content: String!,
  $description: String!,
  $editor: String!,
  $isPublished: Boolean!,
  $isPrivate: Boolean!,
  $locale: String!,
  $path: String!,
  $tags: [String]!,
  $title: String!
) {
  pages {
    create(
      content: $content,
      description: $description,
      editor: $editor,
      isPublished: $isPublished,
      isPrivate: $isPrivate,
      locale: $locale,
      path: $path,
      tags: $tags,
      title: $title
    ) {
      responseResult {
        succeeded
        errorCode
        slug
        message
      }
      page {
        id
        path
        title
      }
    }
  }
}
"""

UPDATE_MUTATION = """
mutation UpdatePage(
  $id: Int!,
  $content: String!,
  $description: String!,
  $editor: String!,
  $isPublished: Boolean!,
  $isPrivate: Boolean!,
  $locale: String!,
  $path: String!,
  $tags: [String]!,
  $title: String!
) {
  pages {
    update(
      id: $id,
      content: $content,
      description: $description,
      editor: $editor,
      isPublished: $isPublished,
      isPrivate: $isPrivate,
      locale: $locale,
      path: $path,
      tags: $tags,
      title: $title
    ) {
      responseResult {
        succeeded
        errorCode
        slug
        message
      }
      page {
        id
        path
        title
      }
    }
  }
}
"""

GET_PAGE_QUERY = """
query GetPage($path: String!, $locale: String!) {
  pages {
    single(path: $path, locale: $locale) {
      id
      path
      title
    }
  }
}
"""


def strip_front_matter(text: str) -> Tuple[Dict, str]:
    if not text.startswith("---"):
        return {}, text
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.DOTALL)
    if not match:
        return {}, text
    raw_meta, body = match.groups()
    if yaml:
        meta = yaml.safe_load(raw_meta) or {}
    else:
        meta = {}
        for line in raw_meta.splitlines():
            if ":" in line and not line.startswith(" "):
                key, val = line.split(":", 1)
                meta[key.strip()] = val.strip()
    return meta, body


def page_path_for_file(md_file: Path) -> str:
    rel = md_file.relative_to(PAGES_DIR).with_suffix("")
    parts = list(rel.parts)
    if parts == ["home"]:
        return WIKIJS_ROOT_PATH
    return "/".join([WIKIJS_ROOT_PATH] + parts)


def graphql(query: str, variables: Dict) -> Dict:
    headers = {"Content-Type": "application/json"}
    if WIKIJS_TOKEN:
        headers["Authorization"] = f"Bearer {WIKIJS_TOKEN}"
    response = requests.post(WIKIJS_URL, json={"query": query, "variables": variables}, headers=headers, timeout=30)
    response.raise_for_status()
    payload = response.json()
    if "errors" in payload:
        raise RuntimeError(payload["errors"])
    return payload.get("data", {})


def get_existing_page_id(path: str):
    try:
        data = graphql(GET_PAGE_QUERY, {"path": path, "locale": WIKIJS_LOCALE})
        page = data.get("pages", {}).get("single")
        return page.get("id") if page else None
    except Exception:
        return None


def upload_page(md_file: Path) -> str:
    raw = md_file.read_text(encoding="utf-8")
    meta, content = strip_front_matter(raw)
    path = page_path_for_file(md_file)
    title = str(meta.get("title") or md_file.stem.replace("-", " ").title())
    description = str(meta.get("description") or "A Big Dumb Idiot Labs Stankopedia page.")
    tags = meta.get("tags") or ["stankopedia", "big-dumb-idiot-labs"]
    if not isinstance(tags, list):
        tags = [str(tags)]

    variables = {
        "content": content,
        "description": description,
        "editor": "markdown",
        "isPublished": True,
        "isPrivate": False,
        "locale": WIKIJS_LOCALE,
        "path": path,
        "tags": [str(t) for t in tags],
        "title": title,
    }

    if DRY_RUN:
        return f"[DRY-STANK] {path} :: {title}"

    existing_id = get_existing_page_id(path)
    if existing_id:
        variables["id"] = int(existing_id)
        data = graphql(UPDATE_MUTATION, variables)
        result = data["pages"]["update"]["responseResult"]
        action = "UPDATED"
    else:
        data = graphql(CREATE_MUTATION, variables)
        result = data["pages"]["create"]["responseResult"]
        action = "CREATED"

    if not result.get("succeeded"):
        raise RuntimeError(f"{path}: {result.get('message')} ({result.get('errorCode')})")
    return f"[{action}] {path} :: {title}"


def main():
    print("=========================================")
    print("BIG DUMB IDIOT LABS")
    print("STANKOPEDIA IMPORTER")
    print("=========================================")

    if not PAGES_DIR.exists():
        print(f"ERROR: Missing pages directory: {PAGES_DIR}")
        sys.exit(1)

    if not DRY_RUN and not WIKIJS_URL:
        print("ERROR: WIKIJS_URL is missing. Add it to .env")
        sys.exit(1)

    md_files = sorted(PAGES_DIR.rglob("*.md"))
    if not md_files:
        print("ERROR: No Markdown files found. Run generate_stankopedia.py first.")
        sys.exit(1)

    ok = 0
    failed = 0
    for md_file in md_files:
        try:
            print(upload_page(md_file))
            ok += 1
        except Exception as exc:
            print(f"[FAILED] {md_file.relative_to(PAGES_DIR)} :: {exc}")
            failed += 1

    print("=========================================")
    print(f"Processed: {len(md_files)}")
    print(f"Succeeded: {ok}")
    print(f"Failed: {failed}")
    print("STANK LEVEL:", "MAXIMUM" if failed == 0 else "PARTIALLY CONTAMINATED")


if __name__ == "__main__":
    main()
