# tgift_prices

Small Python library for fetching Telegram gift floor prices across multiple marketplaces.

## Documentation

Project documentation is prepared for MkDocs Material and GitHub Pages.

- Local docs source: [`docs/`](docs/)
- MkDocs config: [`mkdocs.yml`](mkdocs.yml)
- GitHub Pages workflow: [`.github/workflows/gh-pages.yml`](.github/workflows/gh-pages.yml)

## Quick Start

Install dependency:

```bash
pip install curl_cffi
```

Basic usage:

```python
from tgift_prices import get_floor, search_gifts, available_gifts

result = get_floor("Heart Locket")
print(result)
```

## Run Docs Locally

```bash
pip install mkdocs-material
mkdocs serve
```

## Publish to GitHub Pages

1. Push the repository to GitHub.
2. In repository settings, open `Pages`.
3. Set source to `GitHub Actions`.
4. Push to `main` or run the docs workflow manually.

The workflow builds the MkDocs Material site and publishes it automatically.
