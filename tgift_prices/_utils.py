from difflib import get_close_matches
from typing import List, Optional

from ._constants import GIFTS


def search_gifts(query: str) -> List[str]:
    query_lower = query.lower()
    return [g for g in GIFTS if query_lower in g.lower()]


def _did_you_mean(name: str, n: int = 3) -> Optional[str]:
    matches = get_close_matches(name, GIFTS, n=n, cutoff=0.3)
    return matches[0] if matches else None


def _validate_gift_name(name: str) -> None:
    if name not in GIFTS:
        suggestion = _did_you_mean(name)
        if suggestion:
            raise ValueError(f"Unknown gift: '{name}'. Did you mean '{suggestion}'?")
        else:
            matches = search_gifts(name[:3])
            if matches:
                matches_str = ", ".join(matches[:5])
                raise ValueError(f"Unknown gift: '{name}'. Maybe you meant: {matches_str}?")
            else:
                raise ValueError(f"Unknown gift: '{name}'. Available: {len(GIFTS)} gifts")
