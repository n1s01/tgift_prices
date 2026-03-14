# API Reference (Draft)

> **⚠️ Disclaimer:** These are the initial functions of an early-stage project. The signatures and return types are subject to change without notice in future versions.

## `get_floor`

Fetch the lowest known floor price for one gift or several gifts.

```python
get_floor(gift, markets=None) -> dict[str, FloorResult]
```

Parameters:

- `gift`: a single gift name as `str` or multiple names as `list[str]`
- `markets`: optional list of marketplace names

Response format:

```python
{
    "<gift_name>": {
        "floor": float | None,
        "value": "TON",
        "marketplace": str | None
    }
}
```

Batch example:

```python
from tgift_prices import get_floor

result = get_floor(["Heart Locket", "Toy Bear"])
print(result)
```

## `search_gifts`

Search the built-in gift catalog by query string.

```python
search_gifts(query: str) -> list[str]
```

Example:

```python
from tgift_prices import search_gifts

matches = search_gifts("cap")
print(matches)
```

## `available_gifts`

Return the full list of supported gifts.

```python
available_gifts() -> list[str]
```

Example:

```python
from tgift_prices import available_gifts

gifts = available_gifts()
print(len(gifts))
```

## Behavior notes

- Validation is performed before a request is sent.
- Empty marketplace results produce `floor=None`.
- Returned value units are always `TON`.
