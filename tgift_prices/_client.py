from curl_cffi import requests
from typing import List, Optional, Dict, Union, cast

from ._constants import DEFAULT_MARKETS, _API_URL, GIFTS
from ._types import FloorResult, Markets
from ._utils import search_gifts as _search_gifts
from ._utils import _validate_gift_name


def _fetch(gift_name: str, markets: Markets) -> FloorResult:
    _validate_gift_name(gift_name)

    payload = {
        "ordering": "PRICE_ASC",
        "page": 1,
        "per_page": 1,
        "collections": [gift_name],
        "markets": markets
    }

    resp = requests.post(_API_URL, json=payload, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    items = data.get("items", [])
    if not items:
        return {
            "floor": None,
            "value": "TON",
            "marketplace": None
        }

    item = items[0]
    price_raw = item.get("price", "0")
    price_ton = int(price_raw) / 1e9 if price_raw and str(price_raw).isdigit() else 0.0

    return {
        "floor": price_ton,
        "value": "TON",
        "marketplace": cast(Optional[str], item.get("marketplace"))
    }


def get_floor(
    gift: Union[str, List[str]],
    markets: Optional[Markets] = None
) -> Dict[str, FloorResult]:
    resolved_markets = markets if markets is not None else DEFAULT_MARKETS.copy()

    if isinstance(gift, str):
        return {gift: _fetch(gift, resolved_markets)}
    else:
        return {name: _fetch(name, resolved_markets) for name in gift}


def search_gifts(query: str) -> List[str]:
    return _search_gifts(query)


def available_gifts() -> List[str]:
    return GIFTS.copy()

