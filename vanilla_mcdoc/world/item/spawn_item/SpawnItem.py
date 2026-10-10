"""
Generated from symbols.json for ::java::world::item::spawn_item::SpawnItem
Local link to file: vanilla_mcdoc/world/item/spawn_item/SpawnItem.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.item.ItemBase import ItemBase

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.AnyEntity import AnyEntity


class SpawnItem(ItemBase):
    EntityTag: AnyEntity | None = None  # Data of the spawned entity.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::spawn_item::SpawnItem": {
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
                "desc": "Data of the spawned entity.",
                "key": "EntityTag",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::AnyEntity"
                },
                "optional": True
            }
        ]
    }
}
