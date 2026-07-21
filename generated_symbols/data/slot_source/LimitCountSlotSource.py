# Generated from symbols.json for ::java::data::slot_source::LimitCountSlotSource
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.slot_source.SlotSource import SlotSource


@dataclass(kw_only=True)
class LimitCountSlotSource:
    slot_source: SlotSource
    limit: Annotated[int, 'Range | Min `1` and above | inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::slot_source::LimitCountSlotSource": {
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
                "key": "limit",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            }
        ]
    }
}

