"""
Generated from symbols.json for ::java::data::slot_source::GroupSlotSource
Local link to file: generated_symbols/data/slot_source/GroupSlotSource.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.slot_source.SlotSource import SlotSource


class GroupSlotSource(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'slot_source'

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

