"""
Generated from symbols.json for ::java::assets::item_definition::RangeDispatch
Local link to file: generated_symbols/assets/item_definition/RangeDispatch.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.CompassTarget import CompassTarget
    from generated_symbols.assets.item_definition.ItemModel import ItemModel
    from generated_symbols.assets.item_definition.NumericPropertyType import NumericPropertyType
    from generated_symbols.assets.item_definition.TimeSource import TimeSource
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
class RangeDispatchCompass:
    property: Literal['minecraft:compass']
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None
    target: CompassTarget
    wobble: bool | None = None  # Whether to oscillate for some time around target before settling. Defaults to true.


@dataclass(kw_only=True)
class RangeDispatchCount:
    property: Literal['minecraft:count']
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None
    normalize: bool | None = None  # If false, returns count clamped to `0..max_stack_size`. If true, returns count divided by the `max_stack_size` component, clamped to `0..1`. Defaults to true.


@dataclass(kw_only=True)
class RangeDispatchCustomModelData:
    property: Literal['minecraft:custom_model_data']
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None
    index: Annotated[int, 'Range | `0` and above | inclusive'] | None = None  # The index of the `floats` list in the `custom_model_data` component. Defaults to 0.


@dataclass(kw_only=True)
class RangeDispatchDamage:
    property: Literal['minecraft:damage']
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None
    normalize: bool | None = None  # If false, returns value of damage, clamped to `0..max_damage`. If true, returns value of damage divided by the `max_damage` component, clamped to `0..1`. Defaults to true.


@dataclass(kw_only=True)
class RangeDispatchTime:
    property: Literal['minecraft:time']
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None
    source: TimeSource
    wobble: bool | None = None  # Whether to oscillate for some time around target before settling. Defaults to true.


@dataclass(kw_only=True)
class RangeDispatchUseCycle:
    property: Literal['minecraft:use_cycle']
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None
    period: float | None = None  # returns remaining item use ticks modulo `period`. Defaults to 1.


@dataclass(kw_only=True)
class RangeDispatchUseDuration:
    property: Literal['minecraft:use_duration']
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None
    remaining: bool | None = None  # If true, returns remaining item use ticks. If false, returns item use ticks so far. Defaults to false.


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

