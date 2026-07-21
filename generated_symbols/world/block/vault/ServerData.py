# Generated from symbols.json for ::java::world::block::vault::ServerData
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.item.ItemStack import ItemStack


@dataclass(kw_only=True)
class ServerData:
    state_updating_resumes_at: int | None = None  # Ticks until the loot table is ran again to update the display item.
    rewarded_players: list[tuple[int, int, int, int]] | None = None  # When a player is in this list they can no longer open the vault, but other players can.
    items_to_eject: list[ItemStack] | None = None  # Items that are being ejected from the vault when it is opened. As each item is ejected, it is removed from this list, before ejection, it is previewed as the `display_item`.
    total_ejections_needed: int | None = None  # Number of items that the loot table started off the opening with, does not change while items are ejected.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::vault::ServerData": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Ticks until the loot table is ran again to update the display item.",
                "key": "state_updating_resumes_at",
                "type": {
                    "kind": "long"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "When a player is in this list they can no longer open the vault, but other players can.",
                "key": "rewarded_players",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "int_array",
                        "lengthRange": {
                            "kind": 0,
                            "min": 4,
                            "max": 4
                        }
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Items that are being ejected from the vault when it is opened. As each item is ejected, it is removed from this list, before ejection, it is previewed as the `display_item`.",
                "key": "items_to_eject",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::item::ItemStack"
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Number of items that the loot table started off the opening with, does not change while items are ejected.",
                "key": "total_ejections_needed",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}

