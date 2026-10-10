"""
Generated from symbols.json for ::java::assets::item_definition::RangeDispatch
Local link to file: vanilla_mcdoc/assets/item_definition/RangeDispatch.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Literal

from vanilla_mcdoc.assets.item_definition.Compass import Compass
from vanilla_mcdoc.assets.item_definition.Count import Count
from vanilla_mcdoc.assets.item_definition.CustomModelDataFloats import CustomModelDataFloats
from vanilla_mcdoc.assets.item_definition.Damage import Damage
from vanilla_mcdoc.assets.item_definition.Time import Time
from vanilla_mcdoc.assets.item_definition.UseCycle import UseCycle
from vanilla_mcdoc.assets.item_definition.UseDuration import UseDuration
from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.item_definition.ItemModel import ItemModel
    from vanilla_mcdoc.assets.item_definition.NumericPropertyType import NumericPropertyType
    from vanilla_mcdoc.world.entity.display.Transformation import Transformation


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
