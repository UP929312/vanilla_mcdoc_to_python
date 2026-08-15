"""
Generated from symbols.json for ::java::data::recipe::ItemResult
Local link to file: generated_symbols/data/recipe/ItemResult.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.registry.KnownItemId import KnownItemId


@dataclass(kw_only=True)
class ItemResult:
    item: Annotated[str, IdSpec(registry='item')] | KnownItemId
    count: int | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::ItemResult": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "item",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "item"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "count",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}

