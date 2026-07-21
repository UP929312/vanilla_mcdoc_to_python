# Generated from symbols.json for ::java::data::slot_source::FilterSlotSource
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate
    from generated_symbols.data.slot_source.SlotSource import SlotSource


@dataclass(kw_only=True)
class FilterSlotSource:
    slot_source: SlotSource
    item_filter: ItemPredicate


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::slot_source::FilterSlotSource": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "slot_source",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::slot_source::SlotSource"
                }
            },
            {
                "kind": "pair",
                "key": "item_filter",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::ItemPredicate"
                }
            }
        ]
    }
}

