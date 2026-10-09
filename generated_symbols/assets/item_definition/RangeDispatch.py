"""
Generated from symbols.json for ::java::assets::item_definition::RangeDispatch
Local link to file: generated_symbols/assets/item_definition/RangeDispatch.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Literal

from generated_symbols.assets.item_definition.Compass import Compass
from generated_symbols.assets.item_definition.Count import Count
from generated_symbols.assets.item_definition.CustomModelDataFloats import CustomModelDataFloats
from generated_symbols.assets.item_definition.Damage import Damage
from generated_symbols.assets.item_definition.Time import Time
from generated_symbols.assets.item_definition.UseCycle import UseCycle
from generated_symbols.assets.item_definition.UseDuration import UseDuration
from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.ItemModel import ItemModel
    from generated_symbols.assets.item_definition.NumericPropertyType import NumericPropertyType
    from generated_symbols.world.entity.display.Transformation import Transformation


class EntriesStruct(GeneratedModel):
    threshold: float
    model: ItemModel


class RangeDispatchUnknown(GeneratedModel):
    property: NumericPropertyType
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


class RangeDispatchCompass(Compass):
    property: Literal['minecraft:compass', 'compass'] = 'minecraft:compass'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


class RangeDispatchCount(Count):
    property: Literal['minecraft:count', 'count'] = 'minecraft:count'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


class RangeDispatchCustomModelData(CustomModelDataFloats):
    property: Literal['minecraft:custom_model_data', 'custom_model_data'] = 'minecraft:custom_model_data'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


class RangeDispatchDamage(Damage):
    property: Literal['minecraft:damage', 'damage'] = 'minecraft:damage'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


class RangeDispatchTime(Time):
    property: Literal['minecraft:time', 'time'] = 'minecraft:time'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


class RangeDispatchUseCycle(UseCycle):
    property: Literal['minecraft:use_cycle', 'use_cycle'] = 'minecraft:use_cycle'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


class RangeDispatchUseDuration(UseDuration):
    property: Literal['minecraft:use_duration', 'use_duration'] = 'minecraft:use_duration'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


type RangeDispatch = RangeDispatchUnknown | RangeDispatchCompass | RangeDispatchCount | RangeDispatchCustomModelData | RangeDispatchDamage | RangeDispatchTime | RangeDispatchUseCycle | RangeDispatchUseDuration


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::RangeDispatch": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "property",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::NumericPropertyType",
                    "attributes": [
                        {
                            "name": "id"
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
                                "property"
                            ]
                        }
                    ],
                    "registry": "minecraft:numeric_item_property"
                }
            },
            {
                "kind": "pair",
                "desc": "Factor to multiply the property value with. Defaults to 1.",
                "key": "scale",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "List of ranges. Will select last entry with threshold less or equal to value.\nOrder does not matter, list will be sorted by threshold in ascending order.",
                "key": "entries",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "struct",
                        "fields": [
                            {
                                "kind": "pair",
                                "key": "threshold",
                                "type": {
                                    "kind": "float"
                                }
                            },
                            {
                                "kind": "pair",
                                "key": "model",
                                "type": {
                                    "kind": "reference",
                                    "path": "::java::assets::item_definition::ItemModel"
                                }
                            }
                        ]
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "Item model to render if no entries were less or equal to the value.",
                "key": "fallback",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::ItemModel"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "key": "transformation",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::display::Transformation"
                },
                "optional": True
            }
        ]
    }
}

