# Справочник API

## `get_floor`

Возвращает минимально известную цену (floor) для одного или нескольких подарков.

```python
get_floor(gift, markets=None) -> dict[str, FloorResult]
```

Параметры:

- `gift`: имя одного подарка как `str` или несколько имен как `list[str]`
- `markets`: необязательный список названий торговых площадок

Формат ответа:

```python
{
    "<gift_name>": {
        "floor": float | None,
        "value": "TON",
        "marketplace": str | None
    }
}
```

Пример пакетного запроса:

```python
from tgift_prices import get_floor

result = get_floor(["Heart Locket", "Toy Bear"])
print(result)
```

## `search_gifts`

Поиск по встроенному каталогу подарков по строке запроса.

```python
search_gifts(query: str) -> list[str]
```

Пример:

```python
from tgift_prices import search_gifts

matches = search_gifts("cap")
print(matches)
```

## `available_gifts`

Возвращает полный список поддерживаемых подарков.

```python
available_gifts() -> list[str]
```

Пример:

```python
from tgift_prices import available_gifts

gifts = available_gifts()
print(len(gifts))
```

## Особенности поведения

- Валидация выполняется до отправки запроса.
- Если результатов с площадок нет, возвращается `floor=None`.
- Единицы измерения возвращаемого значения всегда `TON`.
