"""
Generated from symbols.json for ::java::data::advancement::predicate::EntityEquipmentPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/EntityEquipmentPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.predicate.EquipmentPredicateSlot import EquipmentPredicateSlot
    from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate


type EntityEquipmentPredicate = dict[EquipmentPredicateSlot, ItemPredicate]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::EntityEquipmentPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::EquipmentPredicateSlot"
                },
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::ItemPredicate"
                }
            }
        ]
    }
}
