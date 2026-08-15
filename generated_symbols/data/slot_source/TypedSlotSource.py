"""
Generated from symbols.json for ::java::data::slot_source::TypedSlotSource
Local link to file: generated_symbols/data/slot_source/TypedSlotSource.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate
    from generated_symbols.data.loot.BlockEntityTarget import BlockEntityTarget
    from generated_symbols.data.loot.EntityTarget import EntityTarget
    from generated_symbols.data.loot.function.ContainerComponents import ContainerComponents
    from generated_symbols.data.slot_source.SlotSource import SlotSource


@dataclass(kw_only=True)
class TypedSlotSourceContents:
    type: Literal['minecraft:contents']
    slot_source: SlotSource  # The slots to search.
    component: ContainerComponents  # If an item targeted by `slot_source` has this container component, selects all items inside.


@dataclass(kw_only=True)
class TypedSlotSourceEmpty:
    type: Literal['minecraft:empty']


@dataclass(kw_only=True)
class TypedSlotSourceFiltered:
    type: Literal['minecraft:filtered']
    slot_source: SlotSource
    item_filter: ItemPredicate


@dataclass(kw_only=True)
class TypedSlotSourceGroup:
    type: Literal['minecraft:group']
    terms: SlotSource


@dataclass(kw_only=True)
class TypedSlotSourceLimitSlots:
    type: Literal['minecraft:limit_slots']
    slot_source: SlotSource
    limit: Annotated[int, 'Range | Min `1` and above | inclusive']


@dataclass(kw_only=True)
class TypedSlotSourceSlotRange:
    type: Literal['minecraft:slot_range']
    source: EntityTarget | BlockEntityTarget | Literal['container'] | None = None  # Defaults to `container`.
    slots: str


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

