# С чего начать

## Установка зависимостей

Проект использует `curl_cffi` для HTTP-запросов.

```bash
pip install curl_cffi
```

## Импорт публичного API

```python
from tgift_prices import get_floor, search_gifts, available_gifts
```

## Получение минимальной цены для одного подарка

```python
from tgift_prices import get_floor

result = get_floor("Heart Locket", ["TONNEL", "MRKT"])
print(result)
```

Формат ответа:

```python
{
    "<gift_name>": {
        "floor": float | None,
        "value": str,
        "marketplace": str | None
    }
}
```

## Получение минимальных цен для нескольких подарков

```python
from tgift_prices import get_floor

result = get_floor(
    ["Heart Locket", "Durov's Cap"],
    ["TONNEL", "GETGEMS", "THERMOS"]
)
print(result)
```

## Использование торговых площадок по умолчанию

Если параметр `markets` не указан, библиотека использует внутренний список по умолчанию:

```python
["TONNEL", "MRKT", "PORTALS", "GETGEMS", "THERMOS", "THERMOS_ONCHAIN"]
```

```python
from tgift_prices import get_floor

result = get_floor("Heart Locket")
print(result)
```

## Поиск подарков по тексту

```python
from tgift_prices import search_gifts

result = search_gifts("heart")
print(result)
```

Формат ответа:

```python
["<gift_name>", "<gift_name>"]
```

## Получение всех поддерживаемых подарков

```python
from tgift_prices import available_gifts

result = available_gifts()
print(result)
```

## Примечания

- `gift` принимает либо строку, либо список строк.
- `markets` должен быть списком названий торговых площадок.
- Неизвестные названия подарков вызывают исключение `ValueError`.
- Если объявление не найдено, поля `floor` и `marketplace` будут равны `None`.
