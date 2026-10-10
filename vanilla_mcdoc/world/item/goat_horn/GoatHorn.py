"""
Generated from symbols.json for ::java::world::item::goat_horn::GoatHorn
Local link to file: vanilla_mcdoc/world/item/goat_horn/GoatHorn.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.world.item.ItemBase import ItemBase


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
