"""
Generated from symbols.json for ::java::data::slot_source::FilterSlotSource
Local link to file: vanilla_mcdoc/data/slot_source/FilterSlotSource.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
    from vanilla_mcdoc.data.slot_source.SlotSource import SlotSource


class FilterSlotSource(GeneratedModel):
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
