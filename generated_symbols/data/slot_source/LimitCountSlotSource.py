"""
Generated from symbols.json for ::java::data::slot_source::LimitCountSlotSource
Local link to file: generated_symbols/data/slot_source/LimitCountSlotSource.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from generated_symbols.base import GeneratedModel
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.data.slot_source.SlotSource import SlotSource


class LimitCountSlotSource(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'slot_source'

    slot_source: SlotSource
    limit: Annotated[int, Field(ge=1)]


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

