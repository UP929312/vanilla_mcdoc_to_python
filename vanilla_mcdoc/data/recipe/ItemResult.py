"""
Generated from symbols.json for ::java::data::recipe::ItemResult
Local link to file: vanilla_mcdoc/data/recipe/ItemResult.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownItemId import KnownItemId


class ItemResult(GeneratedModel):
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
