"""
Generated from symbols.json for ::java::assets::item_definition::ItemModel
Local link to file: generated_symbols/assets/item_definition/ItemModel.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Field

from generated_symbols.assets.item_definition.BlockState import BlockState
from generated_symbols.assets.item_definition.ChargeType import ChargeType
from generated_symbols.assets.item_definition.Compass import Compass
from generated_symbols.assets.item_definition.ComponentFlags import ComponentFlags
from generated_symbols.assets.item_definition.ComponentStrings import ComponentStrings
from generated_symbols.assets.item_definition.Composite import Composite
from generated_symbols.assets.item_definition.ContextDimension import ContextDimension
from generated_symbols.assets.item_definition.ContextEntityType import ContextEntityType
from generated_symbols.assets.item_definition.Count import Count
from generated_symbols.assets.item_definition.CustomModelDataFlags import CustomModelDataFlags
from generated_symbols.assets.item_definition.CustomModelDataFloats import CustomModelDataFloats
from generated_symbols.assets.item_definition.CustomModelDataStrings import CustomModelDataStrings
from generated_symbols.assets.item_definition.Damage import Damage
from generated_symbols.assets.item_definition.DisplayContext import DisplayContext
from generated_symbols.assets.item_definition.HasComponent import HasComponent
from generated_symbols.assets.item_definition.KeybindDown import KeybindDown
from generated_symbols.assets.item_definition.LocalTime import LocalTime
from generated_symbols.assets.item_definition.MainHand import MainHand
from generated_symbols.assets.item_definition.Model import Model
from generated_symbols.assets.item_definition.SelectCases import SelectCases
from generated_symbols.assets.item_definition.Special import Special
from generated_symbols.assets.item_definition.Time import Time
from generated_symbols.assets.item_definition.TrimMaterial import TrimMaterial
from generated_symbols.assets.item_definition.UseCycle import UseCycle
from generated_symbols.assets.item_definition.UseDuration import UseDuration
from generated_symbols.assets.item_definition.ViewEntity import ViewEntity
from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.ConditionalPropertyType import ConditionalPropertyType
    from generated_symbols.assets.item_definition.NumericPropertyType import NumericPropertyType
    from generated_symbols.assets.item_definition.SelectPropertyType import SelectPropertyType
    from generated_symbols.world.entity.display.Transformation import Transformation


class EntriesStruct(GeneratedModel):
    threshold: float
    model: ItemModel


class ItemModelBundleSelectedItem(GeneratedModel):
    type: Literal['minecraft:bundle/selected_item', 'bundle/selected_item'] = 'minecraft:bundle/selected_item'


class ItemModelComposite(Composite):
    type: Literal['minecraft:composite', 'composite'] = 'minecraft:composite'


class ItemModelConditionUnknown(GeneratedModel):
    type: Literal['minecraft:condition', 'condition'] = 'minecraft:condition'
    property: ConditionalPropertyType
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


class ItemModelConditionComponent(ComponentFlags):
    type: Literal['minecraft:condition', 'condition'] = 'minecraft:condition'
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


class ItemModelConditionCustomModelData(CustomModelDataFlags):
    type: Literal['minecraft:condition', 'condition'] = 'minecraft:condition'
    property: Literal['minecraft:custom_model_data', 'custom_model_data'] = 'minecraft:custom_model_data'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


class ItemModelConditionHasComponent(HasComponent):
    type: Literal['minecraft:condition', 'condition'] = 'minecraft:condition'
    property: Literal['minecraft:has_component', 'has_component'] = 'minecraft:has_component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


class ItemModelConditionKeybindDown(KeybindDown):
    type: Literal['minecraft:condition', 'condition'] = 'minecraft:condition'
    property: Literal['minecraft:keybind_down', 'keybind_down'] = 'minecraft:keybind_down'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


class ItemModelConditionViewEntity(ViewEntity):
    type: Literal['minecraft:condition', 'condition'] = 'minecraft:condition'
    property: Literal['minecraft:view_entity', 'view_entity'] = 'minecraft:view_entity'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


type ItemModelCondition = ItemModelConditionUnknown | ItemModelConditionComponent | ItemModelConditionCustomModelData | ItemModelConditionHasComponent | ItemModelConditionKeybindDown | ItemModelConditionViewEntity

class ItemModelModel(Model):
    type: Literal['minecraft:model', 'model'] = 'minecraft:model'


class ItemModelRangeDispatchUnknown(GeneratedModel):
    type: Literal['minecraft:range_dispatch', 'range_dispatch'] = 'minecraft:range_dispatch'
    property: NumericPropertyType
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


class ItemModelRangeDispatchCompass(Compass):
    type: Literal['minecraft:range_dispatch', 'range_dispatch'] = 'minecraft:range_dispatch'
    property: Literal['minecraft:compass', 'compass'] = 'minecraft:compass'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


class ItemModelRangeDispatchCount(Count):
    type: Literal['minecraft:range_dispatch', 'range_dispatch'] = 'minecraft:range_dispatch'
    property: Literal['minecraft:count', 'count'] = 'minecraft:count'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


class ItemModelRangeDispatchCustomModelData(CustomModelDataFloats):
    type: Literal['minecraft:range_dispatch', 'range_dispatch'] = 'minecraft:range_dispatch'
    property: Literal['minecraft:custom_model_data', 'custom_model_data'] = 'minecraft:custom_model_data'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


class ItemModelRangeDispatchDamage(Damage):
    type: Literal['minecraft:range_dispatch', 'range_dispatch'] = 'minecraft:range_dispatch'
    property: Literal['minecraft:damage', 'damage'] = 'minecraft:damage'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


class ItemModelRangeDispatchTime(Time):
    type: Literal['minecraft:range_dispatch', 'range_dispatch'] = 'minecraft:range_dispatch'
    property: Literal['minecraft:time', 'time'] = 'minecraft:time'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


class ItemModelRangeDispatchUseCycle(UseCycle):
    type: Literal['minecraft:range_dispatch', 'range_dispatch'] = 'minecraft:range_dispatch'
    property: Literal['minecraft:use_cycle', 'use_cycle'] = 'minecraft:use_cycle'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


class ItemModelRangeDispatchUseDuration(UseDuration):
    type: Literal['minecraft:range_dispatch', 'range_dispatch'] = 'minecraft:range_dispatch'
    property: Literal['minecraft:use_duration', 'use_duration'] = 'minecraft:use_duration'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


type ItemModelRangeDispatch = ItemModelRangeDispatchUnknown | ItemModelRangeDispatchCompass | ItemModelRangeDispatchCount | ItemModelRangeDispatchCustomModelData | ItemModelRangeDispatchDamage | ItemModelRangeDispatchTime | ItemModelRangeDispatchUseCycle | ItemModelRangeDispatchUseDuration

class ItemModelSelectUnknown(SelectCases[str]):
    type: Literal['minecraft:select', 'select'] = 'minecraft:select'
    property: SelectPropertyType
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


class ItemModelSelectBlockState(BlockState):
    type: Literal['minecraft:select', 'select'] = 'minecraft:select'
    property: Literal['minecraft:block_state', 'block_state'] = 'minecraft:block_state'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


class ItemModelSelectChargeType(ChargeType):
    type: Literal['minecraft:select', 'select'] = 'minecraft:select'
    property: Literal['minecraft:charge_type', 'charge_type'] = 'minecraft:charge_type'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


class ItemModelSelectComponent(ComponentStrings):
    type: Literal['minecraft:select', 'select'] = 'minecraft:select'
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


class ItemModelSelectContextDimension(ContextDimension):
    type: Literal['minecraft:select', 'select'] = 'minecraft:select'
    property: Literal['minecraft:context_dimension', 'context_dimension'] = 'minecraft:context_dimension'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


class ItemModelSelectContextEntityType(ContextEntityType):
    type: Literal['minecraft:select', 'select'] = 'minecraft:select'
    property: Literal['minecraft:context_entity_type', 'context_entity_type'] = 'minecraft:context_entity_type'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


class ItemModelSelectCustomModelData(CustomModelDataStrings):
    type: Literal['minecraft:select', 'select'] = 'minecraft:select'
    property: Literal['minecraft:custom_model_data', 'custom_model_data'] = 'minecraft:custom_model_data'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


class ItemModelSelectDisplayContext(DisplayContext):
    type: Literal['minecraft:select', 'select'] = 'minecraft:select'
    property: Literal['minecraft:display_context', 'display_context'] = 'minecraft:display_context'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


class ItemModelSelectLocalTime(LocalTime):
    type: Literal['minecraft:select', 'select'] = 'minecraft:select'
    property: Literal['minecraft:local_time', 'local_time'] = 'minecraft:local_time'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


class ItemModelSelectMainHand(MainHand):
    type: Literal['minecraft:select', 'select'] = 'minecraft:select'
    property: Literal['minecraft:main_hand', 'main_hand'] = 'minecraft:main_hand'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


class ItemModelSelectTrimMaterial(TrimMaterial):
    type: Literal['minecraft:select', 'select'] = 'minecraft:select'
    property: Literal['minecraft:trim_material', 'trim_material'] = 'minecraft:trim_material'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


type ItemModelSelect = ItemModelSelectUnknown | ItemModelSelectBlockState | ItemModelSelectChargeType | ItemModelSelectComponent | ItemModelSelectContextDimension | ItemModelSelectContextEntityType | ItemModelSelectCustomModelData | ItemModelSelectDisplayContext | ItemModelSelectLocalTime | ItemModelSelectMainHand | ItemModelSelectTrimMaterial

class ItemModelSpecial(Special):
    type: Literal['minecraft:special', 'special'] = 'minecraft:special'


type ItemModel = Annotated[
    ItemModelBundleSelectedItem | ItemModelComposite | ItemModelCondition | ItemModelModel | ItemModelRangeDispatch | ItemModelSelect | ItemModelSpecial,
    Field(discriminator='type'),
]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::ItemModel": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::ItemModeltype",
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
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:item_model"
                }
            }
        ]
    }
}

