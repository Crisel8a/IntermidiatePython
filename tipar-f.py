def suma_clara(a: int, b: int) -> int:
    return a + b


articles: list[dict] = [
    {"title": "Example"},
    {"title": "Example 2"},
]

articles_dos: list[list[str]] = [
    ["articulos", "otros"],
    ["articulos", "otros"],
]

from typing import Any

articles_tres: list[list[Any]] = [
    ["articulos", "otros", 123],
    ["articulos", "otros"],
]

# int, str, list, dict, tuple, Any
