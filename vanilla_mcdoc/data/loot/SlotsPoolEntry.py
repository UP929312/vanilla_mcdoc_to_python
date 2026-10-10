"""
Generated from symbols.json for ::java::data::loot::SlotsPoolEntry
Local link to file: vanilla_mcdoc/data/loot/SlotsPoolEntry.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.loot.SingletonPoolEntry import SingletonPoolEntry

if TYPE_CHECKING:
    from vanilla_mcdoc.data.slot_source.SlotSource import SlotSource


class SlotsPoolEntry(SingletonPoolEntry):
    slot_source: SlotSource


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::SlotsPoolEntry": {
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
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::SingletonPoolEntry"
                }
            }
        ]
    }
}
