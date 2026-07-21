# Generated from symbols.json for ::java::world::entity::ominous_item_spawner::OminousItemSpawner
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.EntityBase import EntityBase

if TYPE_CHECKING:
    from generated_symbols.world.item.ItemStack import ItemStack


@dataclass(kw_only=True)
class OminousItemSpawner(EntityBase):
    item: ItemStack | None = None
    spawn_item_after_ticks: int | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::ominous_item_spawner::OminousItemSpawner": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::EntityBase"
                }
            },
            {
                "kind": "pair",
                "key": "item",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemStack"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "spawn_item_after_ticks",
                "type": {
                    "kind": "long"
                },
                "optional": True
            }
        ]
    }
}

