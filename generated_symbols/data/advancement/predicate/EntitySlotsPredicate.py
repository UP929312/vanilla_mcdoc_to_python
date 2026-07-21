# Generated from symbols.json for ::java::data::advancement::predicate::EntitySlotsPredicate
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate


type EntitySlotsPredicate = dict[str, ItemPredicate]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::EntitySlotsPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "item_slots"
                        }
                    ]
                },
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::ItemPredicate"
                }
            }
        ]
    }
}

