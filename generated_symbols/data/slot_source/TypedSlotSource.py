"""
Generated from symbols.json for ::java::data::slot_source::TypedSlotSource
Local link to file: generated_symbols/data/slot_source/TypedSlotSource.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar, Literal

from pydantic import Field

from generated_symbols.base import GeneratedModel
from generated_symbols.data.slot_source.ContentsSlotSource import ContentsSlotSource
from generated_symbols.data.slot_source.FilterSlotSource import FilterSlotSource
from generated_symbols.data.slot_source.GroupSlotSource import GroupSlotSource
from generated_symbols.data.slot_source.LimitCountSlotSource import LimitCountSlotSource
from generated_symbols.data.slot_source.RangeSlotSource import RangeSlotSource


class TypedSlotSourceContents(ContentsSlotSource):
    __resource_dir__: ClassVar[str] = 'slot_source'

    type: Literal['minecraft:contents', 'contents'] = 'minecraft:contents'


class TypedSlotSourceEmpty(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'slot_source'

    type: Literal['minecraft:empty', 'empty'] = 'minecraft:empty'


class TypedSlotSourceFiltered(FilterSlotSource):
    __resource_dir__: ClassVar[str] = 'slot_source'

    type: Literal['minecraft:filtered', 'filtered'] = 'minecraft:filtered'


class TypedSlotSourceGroup(GroupSlotSource):
    __resource_dir__: ClassVar[str] = 'slot_source'

    type: Literal['minecraft:group', 'group'] = 'minecraft:group'


class TypedSlotSourceLimitSlots(LimitCountSlotSource):
    __resource_dir__: ClassVar[str] = 'slot_source'

    type: Literal['minecraft:limit_slots', 'limit_slots'] = 'minecraft:limit_slots'


class TypedSlotSourceSlotRange(RangeSlotSource):
    __resource_dir__: ClassVar[str] = 'slot_source'

    type: Literal['minecraft:slot_range', 'slot_range'] = 'minecraft:slot_range'


type TypedSlotSource = Annotated[
    TypedSlotSourceContents | TypedSlotSourceEmpty | TypedSlotSourceFiltered | TypedSlotSourceGroup | TypedSlotSourceLimitSlots | TypedSlotSourceSlotRange,
    Field(discriminator='type'),
]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::slot_source::TypedSlotSource": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "slot_source_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:slot_source"
                }
            }
        ]
    }
}
