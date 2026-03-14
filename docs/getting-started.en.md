# Getting Started

## Install dependency

The project uses `curl_cffi` for HTTP requests.

```bash
pip install curl_cffi
```

## Import the public API

```python
from tgift_prices import get_floor, search_gifts, available_gifts
```

## Get the floor price for one gift

```python
from tgift_prices import get_floor

result = get_floor("Heart Locket", ["TONNEL", "MRKT"])
print(result)
```

Return shape:

```python
{
    "<gift_name>": {
        "floor": float | None,
        "value": str,
        "marketplace": str | None
    }
}
```

## Get floor prices for multiple gifts

```python
from tgift_prices import get_floor

result = get_floor(
    ["Heart Locket", "Durov's Cap"],
    ["TONNEL", "GETGEMS", "THERMOS"]
)
print(result)
```

## Use default marketplaces

If `markets` is omitted, the library uses the internal default list:

```python
["TONNEL", "MRKT", "PORTALS", "GETGEMS", "THERMOS", "THERMOS_ONCHAIN"]
```

```python
from tgift_prices import get_floor

result = get_floor("Heart Locket")
print(result)
```

## Search gifts by text

```python
from tgift_prices import search_gifts

result = search_gifts("heart")
print(result)
```

Return shape:

```python
["<gift_name>", "<gift_name>"]
```

## Get all supported gifts

```python
from tgift_prices import available_gifts

result = available_gifts()
print(result)
```

## Notes

- `gift` accepts either a string or a list of strings.
- `markets` must be a list of marketplace names.
- Unknown gift names raise `ValueError`.
- If no listing is found, `floor` and `marketplace` are `None`.
