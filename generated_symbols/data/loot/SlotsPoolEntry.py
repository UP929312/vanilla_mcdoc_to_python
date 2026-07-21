# Generated from symbols.json for ::java::data::loot::SlotsPoolEntry
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.loot.SingletonPoolEntry import SingletonPoolEntry

if TYPE_CHECKING:
    from generated_symbols.data.slot_source.SlotSource import SlotSource


@dataclass(kw_only=True)
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

