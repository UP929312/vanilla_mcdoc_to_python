# Generated from symbols.json for ::java::world::entity::mob::DropChances
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.util.slot.EquipmentSlot import EquipmentSlot


type DropChances = dict[EquipmentSlot, Annotated[float, 'Range | Min `0` and above | inclusive']]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::DropChances": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "`0.0` is hardcoded to be unaffected by enchantments. \\\nValues between `0.0` and `1.0` (inclusive) randomizes durability of the dropped item.",
                "key": {
                    "kind": "reference",
                    "path": "::java::util::slot::EquipmentSlot"
                },
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                }
            }
        ]
    }
}

