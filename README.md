# tgift_prices

`tgift_prices` is a small Python library for getting Telegram gift floor prices.

## Install

```bash
pip install curl_cffi
```

## Import

```python
from tgift_prices import get_floor, search_gifts, available_gifts
```

## How to use

### Get floor for one gift

```python
from tgift_prices import get_floor

result = get_floor("<gift_name>", ["<market>", "<market>"])
print(result)
```

Return format:

```python
{
    '<gift_name>': {
        'floor': float | None,
        'value': str,
        'marketplace': str | None
    }
}
```

### Get floor for multiple gifts

```python
from tgift_prices import get_floor

result = get_floor(["<gift_name>", "<gift_name>"], ["<market>", "<market>"])
print(result)
```

Return format:

```python
{
    '<gift_name>': {
        'floor': float | None,
        'value': str,
        'marketplace': str | None
    },
    '<gift_name>': {
        'floor': float | None,
        'value': str,
        'marketplace': str | None
    }
}
```

### Use default markets

```python
from tgift_prices import get_floor

result = get_floor("<gift_name>")
print(result)
```

If `markets` is not passed, the library uses default markets.

### Search gifts

```python
from tgift_prices import search_gifts

result = search_gifts("<query>")
print(result)
```

Return format:

```python
['<gift_name>', '<gift_name>']
```

### Get all available gifts

```python
from tgift_prices import available_gifts

result = available_gifts()
print(result)
```

Return format:

```python
['<gift_name>', '<gift_name>']
```

## Notes

- `gift` can be a string or a list of strings.
- `markets` must be a list of marketplace names.
- If a gift is not found in the internal gift list, the library raises `ValueError`.
- If no listing is found, `floor` and `marketplace` return `None`.
