# Generated from symbols.json for ::java::world::block::vault::SharedData
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.item.ItemStack import ItemStack


@dataclass(kw_only=True)
class SharedData:
    display_item: ItemStack | None = None  # Item that is displayed to players when they are in range of the vault.
    connected_players: list[tuple[int, int, int, int]] | None = None
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

