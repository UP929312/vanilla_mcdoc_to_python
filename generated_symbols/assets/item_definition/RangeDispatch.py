"""
Generated from symbols.json for ::java::assets::item_definition::RangeDispatch
Local link to file: generated_symbols/assets/item_definition/RangeDispatch.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from generated_symbols.assets.item_definition.Compass import Compass
from generated_symbols.assets.item_definition.Count import Count
from generated_symbols.assets.item_definition.CustomModelDataFloats import CustomModelDataFloats
from generated_symbols.assets.item_definition.Damage import Damage
from generated_symbols.assets.item_definition.Time import Time
from generated_symbols.assets.item_definition.UseCycle import UseCycle
from generated_symbols.assets.item_definition.UseDuration import UseDuration

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.ItemModel import ItemModel
    from generated_symbols.assets.item_definition.NumericPropertyType import NumericPropertyType
    from generated_symbols.world.entity.display.Transformation import Transformation


@dataclass(kw_only=True)
class EntriesStruct:
    threshold: float
    model: ItemModel


@dataclass(kw_only=True)
class RangeDispatchUnknown:
    property: NumericPropertyType
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class RangeDispatchCompass(Compass):
    property: Literal['minecraft:compass'] = 'minecraft:compass'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class RangeDispatchCount(Count):
    property: Literal['minecraft:count'] = 'minecraft:count'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class RangeDispatchCustomModelData(CustomModelDataFloats):
    property: Literal['minecraft:custom_model_data'] = 'minecraft:custom_model_data'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class RangeDispatchDamage(Damage):
    property: Literal['minecraft:damage'] = 'minecraft:damage'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class RangeDispatchTime(Time):
    property: Literal['minecraft:time'] = 'minecraft:time'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class RangeDispatchUseCycle(UseCycle):
    property: Literal['minecraft:use_cycle'] = 'minecraft:use_cycle'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class RangeDispatchUseDuration(UseDuration):
    property: Literal['minecraft:use_duration'] = 'minecraft:use_duration'
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

