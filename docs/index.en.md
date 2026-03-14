# tgift_prices

> Fast access to Telegram gift floor prices from multiple marketplaces.

`tgift_prices` is a compact Python library for three simple tasks:

- get the lowest price for one or more gifts
- search gift names from the built-in catalog
- retrieve the full list of available gifts

<div class="hero-grid" markdown>

<div class="hero-card" markdown>
### Multi-market floor lookup
Query marketplaces like `TONNEL`, `MRKT`, `PORTALS`, `GETGEMS`, `THERMOS`, and `THERMOS_ONCHAIN`.
</div>

<div class="hero-card" markdown>
### Minimal public API
Import only three functions: `get_floor`, `search_gifts`, `available_gifts`.
</div>

<div class="hero-card" markdown>
### Ready for automation
Useful for bots, dashboards, scripts, and Telegram gift market monitoring.
</div>

</div>

## Quick Example

```python
from tgift_prices import get_floor

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

## Why use it

- Small surface area and predictable return shapes
- Default marketplace list out of the box
- Built-in validation against a known gift catalog
- Suitable for single gifts and batch requests

## Next steps

- Start with [Getting Started](getting-started.md)
- See full API usage in [API Reference](api.md)
