"""
Generated from symbols.json for ::java::data::slot_source::FilterSlotSource
Local link to file: generated_symbols/data/slot_source/FilterSlotSource.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate
    from generated_symbols.data.slot_source.SlotSource import SlotSource


@dataclass(kw_only=True)
class FilterSlotSource:
    __resource_dir__: ClassVar[str] = 'slot_source'

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

