"""
Generated from symbols.json for ::java::world::block::vault::SharedData
Local link to file: vanilla_mcdoc/world/block/vault/SharedData.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import MinecraftUUID

if TYPE_CHECKING:
    from vanilla_mcdoc.world.item.ItemStack import ItemStack


class SharedData(GeneratedModel):
    display_item: ItemStack | None = None  # Item that is displayed to players when they are in range of the vault.
    connected_players: list[MinecraftUUID] | None = None
    connected_particles_range: float | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::vault::SharedData": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Item that is displayed to players when they are in range of the vault.",
                "key": "display_item",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemStack"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "connected_players",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "int_array",
                        "lengthRange": {
                            "kind": 0,
                            "min": 4,
                            "max": 4
                        },
                        "attributes": [
                            {
                                "name": "uuid"
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "connected_particles_range",
                "type": {
                    "kind": "double"
                },
                "optional": True
            }
        ]
    }
}
