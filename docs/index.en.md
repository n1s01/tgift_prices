# tgift_prices

# tgift_prices

> **⚠️ Early Alpha:** This project is in its very early stages of development. The current version only includes initial proof-of-concept functions. Features and API structures might change significantly in the future.

A simple Python tool we are building to fetch Telegram gift floor prices from multiple marketplaces.

Currently, `tgift_prices` provides three basic functions:

- get the lowest known price for a gift
- search gift names from an internal list
- retrieve the list of supported gifts

<div class="hero-grid" markdown>

<div class="hero-card" markdown>
### Multi-market lookups
Query marketplaces like `TONNEL`, `MRKT`, `PORTALS`, `GETGEMS`, `THERMOS`, and `THERMOS_ONCHAIN`.
</div>

<div class="hero-card" markdown>
### Basic API structure
Current exposed functions: `get_floor`, `search_gifts`, `available_gifts`.
</div>

<div class="hero-card" markdown>
### Work in Progress
This is not a finished library yet. More features will be added as the project evolves.
</div>

</div>

## Quick Example

```python
from tgift_prices import get_floor

# Fetching the current floor price (returns data or None)
result = get_floor("Heart Locket")
print(result)
```

Example response:

```python
{
    "Heart Locket": {
        "floor": 12.5,
        "value": "TON",
        "marketplace": "TONNEL"
    }
}
```

## Next steps

- See [Getting Started](getting-started.md) to try out the current features.
- See the current function signatures in [API Reference](api.md).
