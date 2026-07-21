# Generated from symbols.json for ::java::data::advancement::predicate::EntityEquipmentPredicate
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate
    from generated_symbols.util.slot.EquipmentSlot import EquipmentSlot


type EntityEquipmentPredicate = dict[EquipmentSlot, ItemPredicate]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::EntityEquipmentPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "reference",
                    "path": "::java::util::slot::EquipmentSlot"
                },
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::ItemPredicate"
                }
            }
        ]
    }
}

