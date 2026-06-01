# Big Dumb Idiot Labs Stankopedia Pack

This creates and uploads 100 fake wiki pages plus a Stankopedia home page into WikiJS.

## Install requirements

```bash
cd /mnt/user/appdata/bigdumbidiot-stankopedia
python3 -m pip install requests python-dotenv pyyaml
```

## Generate pages

```bash
python3 generate_stankopedia.py
```

This creates:

```text
pages/home.md
pages/doctrine/*.md
pages/history/*.md
pages/science/*.md
...
```

## Configure uploader

```bash
cp .env.example .env
nano .env
```

Set:

```bash
WIKIJS_URL=https://your-wiki-domain/graphql
WIKIJS_TOKEN=your_api_token
WIKIJS_LOCALE=en
WIKIJS_ROOT_PATH=stankopedia
```

## Dry run first

```bash
DRY_RUN=true python3 upload_stankopedia.py
```

## Upload the stank

```bash
python3 upload_stankopedia.py
```

Pages will appear under:

```text
/stankopedia
/stankopedia/doctrine/the-beauty-of-stank
/stankopedia/government/the-bathing-agenda
/stankopedia/food/candy-is-very-tasty
```

## Notes

The uploader attempts to update existing pages when paths already exist.
If your WikiJS GraphQL schema differs, the mutation may need a small adjustment.
