# Generated from symbols.json for ::java::world::entity::mob::allay::Allay
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.mob.MobBase import MobBase

if TYPE_CHECKING:
    from generated_symbols.util.game_event.VibrationListener import VibrationListener
    from generated_symbols.world.item.ItemStack import ItemStack


@dataclass(kw_only=True)
class Allay(MobBase):
    DuplicationCooldown: int | None = None  # Ticks until the allay can duplicate. This is set to 6000 game ticks (5 minutes) when the allay duplicates.
    Inventory: tuple[ItemStack] | None = None  # Items it has picked up. Note that the item given by the player is in the allay's `HandItems[0]` tag, not here.
    listener: VibrationListener | None = None  # Vibration game event listener.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::allay::Allay": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::MobBase"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "Whether the allay can duplicate. This is set to False when the allay duplicates.",
                "key": "CanDuplicate",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Ticks until the allay can duplicate. This is set to 6000 game ticks (5 minutes) when the allay duplicates.",
                "key": "DuplicationCooldown",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Items it has picked up. Note that the item given by the player is in\nthe allay's `HandItems[0]` tag, not here.",
                "key": "Inventory",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::item::ItemStack"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 1
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Vibration game event listener.",
                "key": "listener",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::game_event::VibrationListener"
                },
                "optional": True
            }
        ]
    }
}

