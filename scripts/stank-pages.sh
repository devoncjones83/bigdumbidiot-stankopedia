#!/bin/bash
set -euo pipefail

DROP="/mnt/user/stankdrop/pages"
REPO="/mnt/user/appdata/bigdumbidiot-stankopedia"

PAGES="$REPO/pages"
IMAGES="$REPO/images"

mkdir -p "$DROP" "$PAGES" "$IMAGES"

cd "$REPO"

find "$DROP" -mindepth 1 -type f -name "article.md" | sort | while read -r article; do
  src_dir="$(dirname "$article")"
  rel_path="${src_dir#$DROP/}"

  page_dir="$PAGES/$rel_path"
  image_src="$src_dir/images"
  image_dest="$IMAGES/$rel_path"

  mkdir -p "$page_dir" "$image_dest"

  meta="$src_dir/metadata.yml"

  if [ -f "$meta" ]; then
    title="$(grep '^title:' "$meta" | cut -d':' -f2- | sed 's/^ //')"
    classification="$(grep '^classification:' "$meta" | cut -d':' -f2- | sed 's/^ //')"
    threat="$(grep '^threat:' "$meta" | cut -d':' -f2- | sed 's/^ //')"
    status="$(grep '^status:' "$meta" | cut -d':' -f2- | sed 's/^ //')"
  else
    title="$(basename "$src_dir" | sed 's/-/ /g' | sed 's/_/ /g')"
    classification=""
    threat=""
    status=""
  fi

  page="$page_dir/index.md"

  cp "$article" "$page"

  {
    echo ""
    echo "---"
    echo ""
    echo "## Evidence Archive"
    echo ""
  } >> "$page"

  if [ -d "$image_src" ]; then
    find "$image_src" -maxdepth 1 -type f \( \
      -iname "*.png" -o \
      -iname "*.jpg" -o \
      -iname "*.jpeg" -o \
      -iname "*.webp" \
    \) -print0 | while IFS= read -r -d '' img; do
      cp -u "$img" "$image_dest/"
    done
  fi

  if [ -d "$image_dest" ]; then
    find "$image_dest" -maxdepth 1 -type f \( \
      -iname "*.png" -o \
      -iname "*.jpg" -o \
      -iname "*.jpeg" -o \
      -iname "*.webp" \
    \) | sort | while read -r img; do
      file="$(basename "$img")"
      label="$(echo "$file" | sed 's/\.[^.]*$//' | sed 's/_/ /g')"

      cat >> "$page" <<ENTRY
### $label

![${label}](/images/$rel_path/$file)

ENTRY
    done
  fi

  echo "Generated page: $page"
done

git add pages images scripts

if git diff --cached --quiet; then
  echo "No new page stank to commit."
else
  git commit -m "Update generated Stankopedia pages"
  git push origin main
  echo "Committed and pushed generated Stankopedia pages."
fi
