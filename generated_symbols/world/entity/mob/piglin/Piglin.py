# Generated from symbols.json for ::java::world::entity::mob::piglin::Piglin
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated
from generated_symbols.world.entity.mob.piglin.PiglinBase import PiglinBase

if TYPE_CHECKING:
    from generated_symbols.world.item.ItemStack import ItemStack


@dataclass(kw_only=True)
class Piglin(PiglinBase):
    IsBaby: bool | None = None  # Whether it is a baby.
    CannotHunt: bool | None = None  # Whether it does not hunt hoglins.
    Inventory: Annotated[list[ItemStack], 'Length = 0-8 (both inclusive)'] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::piglin::Piglin": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::piglin::PiglinBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Whether it is a baby.",
                "key": "IsBaby",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether it does not hunt hoglins.",
                "key": "CannotHunt",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "Inventory",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::item::ItemStack"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 8
                    }
                },
                "optional": True
            }
        ]
    }
}

