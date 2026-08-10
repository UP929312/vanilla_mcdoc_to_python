"""
Generated from symbols.json for ::java::world::item::goat_horn::GoatHorn
Local link to file: generated_symbols/world/item/goat_horn/GoatHorn.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from generated_symbols.world.item.ItemBase import ItemBase
from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class GoatHorn(ItemBase):
    instrument: Annotated[str, IdSpec(registry='instrument')] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::goat_horn::GoatHorn": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemBase"
                }
            },
            {
                "kind": "pair",
                "key": "instrument",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "instrument"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

