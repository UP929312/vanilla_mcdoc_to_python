# Generated from symbols.json for ::java::data::slot_source::GroupSlotSource
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.slot_source.SlotSource import SlotSource


@dataclass(kw_only=True)
class GroupSlotSource:
    terms: SlotSource


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::slot_source::GroupSlotSource": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "terms",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::slot_source::SlotSource"
                }
            }
        ]
    }
}

