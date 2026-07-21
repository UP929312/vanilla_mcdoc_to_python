# Generated from symbols.json for ::java::world::item::spawn_item::SpawnItem
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.item.ItemBase import ItemBase

if TYPE_CHECKING:
    from generated_symbols.world.entity.AnyEntity import AnyEntity


@dataclass(kw_only=True)
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

