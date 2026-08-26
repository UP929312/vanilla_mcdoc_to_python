"""
Generated from symbols.json for ::java::data::slot_source::TypedSlotSource
Local link to file: generated_symbols/data/slot_source/TypedSlotSource.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import ClassVar, Literal

from generated_symbols.data.slot_source.ContentsSlotSource import ContentsSlotSource
from generated_symbols.data.slot_source.FilterSlotSource import FilterSlotSource
from generated_symbols.data.slot_source.GroupSlotSource import GroupSlotSource
from generated_symbols.data.slot_source.LimitCountSlotSource import LimitCountSlotSource
from generated_symbols.data.slot_source.RangeSlotSource import RangeSlotSource


@dataclass(kw_only=True)
class TypedSlotSourceContents(ContentsSlotSource):
    __resource_dir__: ClassVar[str] = 'slot_source'

    type: Literal['minecraft:contents'] = 'minecraft:contents'


@dataclass(kw_only=True)
class TypedSlotSourceEmpty:
    type: Literal['minecraft:empty'] = 'minecraft:empty'


@dataclass(kw_only=True)
class TypedSlotSourceFiltered(FilterSlotSource):
    type: Literal['minecraft:filtered'] = 'minecraft:filtered'


@dataclass(kw_only=True)
class TypedSlotSourceGroup(GroupSlotSource):
    type: Literal['minecraft:group'] = 'minecraft:group'


@dataclass(kw_only=True)
class TypedSlotSourceLimitSlots(LimitCountSlotSource):
    type: Literal['minecraft:limit_slots'] = 'minecraft:limit_slots'


@dataclass(kw_only=True)
class TypedSlotSourceSlotRange(RangeSlotSource):
    type: Literal['minecraft:slot_range'] = 'minecraft:slot_range'


type TypedSlotSource = TypedSlotSourceContents | TypedSlotSourceEmpty | TypedSlotSourceFiltered | TypedSlotSourceGroup | TypedSlotSourceLimitSlots | TypedSlotSourceSlotRange


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

