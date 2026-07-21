# Generated from symbols.json for ::java::world::entity::mob::breedable::horse::ChestedHorse
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Any
from generated_symbols.world.entity.mob.breedable.horse.HorseBase import HorseBase

if TYPE_CHECKING:
    from generated_symbols.util.slot.SlottedItem import SlottedItem


@dataclass(kw_only=True)
class ChestedHorse(HorseBase):
    ChestedHorse: bool | None = None  # Whether it has a chest.
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`14` | both inclusive']] | Any], 'Length = 0-15 (both inclusive)'] | None = None  # Slots from 0 to 14.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::horse::ChestedHorse": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::horse::HorseBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Whether it has a chest.",
                "key": "ChestedHorse",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Slots from 0 to 14.",
                "key": "Items",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "union",
                        "members": [
                            {
                                "kind": "concrete",
                                "child": {
                                    "kind": "reference",
                                    "path": "::java::util::slot::SlottedItem"
                                },
                                "typeArgs": [
                                    {
                                        "kind": "byte",
                                        "valueRange": {
                                            "kind": 0,
                                            "min": 0,
                                            "max": 14
                                        }
                                    }
                                ]
                            },
                            {
                                "kind": "struct",
                                "fields": []
                            }
                        ]
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 15
                    }
                },
                "optional": True
            }
        ]
    }
}

