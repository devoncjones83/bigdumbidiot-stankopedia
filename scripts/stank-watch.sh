#!/bin/bash
set -euo pipefail

DROP="/mnt/user/stankdrop"
REPO="/mnt/user/appdata/bigdumbidiot-stankopedia"

PAGES="$REPO/pages/wombats/incidents"
IMAGES="$REPO/images/wombats"

mkdir -p "$PAGES" "$IMAGES"

cd "$REPO"

for dir in "$DROP"/WC[0-9][0-9]; do
  [ -d "$dir" ] || continue

  wc="$(basename "$dir")"
  wc_lower="$(echo "$wc" | tr '[:upper:]' '[:lower:]')"

  meta="$dir/metadata.yml"

  if [ ! -f "$meta" ]; then
    cat > "$meta" <<META
title: $wc Untitled Wombat Case
classification: Unclassified Stank Event
threat: Unknown
status: Under Review
META
  fi

  title="$(grep '^title:' "$meta" | cut -d':' -f2- | sed 's/^ //')"
  classification="$(grep '^classification:' "$meta" | cut -d':' -f2- | sed 's/^ //')"
  threat="$(grep '^threat:' "$meta" | cut -d':' -f2- | sed 's/^ //')"
  status="$(grep '^status:' "$meta" | cut -d':' -f2- | sed 's/^ //')"

  page_dir="$PAGES/$wc_lower"
  image_dir="$IMAGES/$wc_lower"

  mkdir -p "$page_dir" "$image_dir"

  find "$dir" -maxdepth 1 -type f \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.webp" \) -print0 \
    | while IFS= read -r -d '' img; do
        cp -u "$img" "$image_dir/"
      done

  page="$page_dir/index.md"

  cat > "$page" <<PAGE
# $title

**Classification:** $classification  
**Containment Status:** $status  
**Threat Level:** $threat  

## Summary

This Wombat Division case file was generated automatically from the stankdrop evidence locker.

## Evidence Archive

PAGE

  find "$image_dir" -maxdepth 1 -type f \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.webp" \) | sort | while read -r img; do
    file="$(basename "$img")"
    label="$(echo "$file" | sed 's/\.[^.]*$//' | sed 's/_/ /g')"

    cat >> "$page" <<ENTRY
### $label

![${label}](/images/wombats/$wc_lower/$file)

ENTRY
  done

  echo "Generated: $page"
done

git add pages/wombats/incidents images/wombats /mnt/user/stankdrop/WC*/metadata.yml 2>/dev/null || true

if git diff --cached --quiet; then
  echo "No new stank to commit."
else
  git commit -m "Generate Wombat Division incident pages"
  echo "Committed stank. Run git push when ready."
fi
