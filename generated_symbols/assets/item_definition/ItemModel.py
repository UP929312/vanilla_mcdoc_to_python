"""
Generated from symbols.json for ::java::assets::item_definition::ItemModel
Local link to file: generated_symbols/assets/item_definition/ItemModel.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

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

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.ConditionalPropertyType import ConditionalPropertyType
    from generated_symbols.assets.item_definition.NumericPropertyType import NumericPropertyType
    from generated_symbols.assets.item_definition.SelectPropertyType import SelectPropertyType
    from generated_symbols.world.entity.display.Transformation import Transformation


@dataclass(kw_only=True)
class EntriesStruct:
    threshold: float
    model: ItemModel


@dataclass(kw_only=True)
class ItemModelBundleSelectedItem:
    type: Literal['minecraft:bundle/selected_item'] = 'minecraft:bundle/selected_item'


@dataclass(kw_only=True)
class ItemModelComposite(Composite):
    type: Literal['minecraft:composite'] = 'minecraft:composite'


@dataclass(kw_only=True)
class ItemModelConditionUnknown:
    type: Literal['minecraft:condition'] = 'minecraft:condition'
    property: ConditionalPropertyType
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelConditionComponent(ComponentFlags):
    type: Literal['minecraft:condition'] = 'minecraft:condition'
    property: Literal['minecraft:component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelConditionCustomModelData(CustomModelDataFlags):
    type: Literal['minecraft:condition'] = 'minecraft:condition'
    property: Literal['minecraft:custom_model_data'] = 'minecraft:custom_model_data'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelConditionHasComponent(HasComponent):
    type: Literal['minecraft:condition'] = 'minecraft:condition'
    property: Literal['minecraft:has_component'] = 'minecraft:has_component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelConditionKeybindDown(KeybindDown):
    type: Literal['minecraft:condition'] = 'minecraft:condition'
    property: Literal['minecraft:keybind_down'] = 'minecraft:keybind_down'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelConditionViewEntity(ViewEntity):
    type: Literal['minecraft:condition'] = 'minecraft:condition'
    property: Literal['minecraft:view_entity'] = 'minecraft:view_entity'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


type ItemModelCondition = ItemModelConditionUnknown | ItemModelConditionComponent | ItemModelConditionCustomModelData | ItemModelConditionHasComponent | ItemModelConditionKeybindDown | ItemModelConditionViewEntity

@dataclass(kw_only=True)
class ItemModelModel(Model):
    type: Literal['minecraft:model'] = 'minecraft:model'


@dataclass(kw_only=True)
class ItemModelRangeDispatchUnknown:
    type: Literal['minecraft:range_dispatch'] = 'minecraft:range_dispatch'
    property: NumericPropertyType
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelRangeDispatchCompass(Compass):
    type: Literal['minecraft:range_dispatch'] = 'minecraft:range_dispatch'
    property: Literal['minecraft:compass'] = 'minecraft:compass'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelRangeDispatchCount(Count):
    type: Literal['minecraft:range_dispatch'] = 'minecraft:range_dispatch'
    property: Literal['minecraft:count'] = 'minecraft:count'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelRangeDispatchCustomModelData(CustomModelDataFloats):
    type: Literal['minecraft:range_dispatch'] = 'minecraft:range_dispatch'
    property: Literal['minecraft:custom_model_data'] = 'minecraft:custom_model_data'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelRangeDispatchDamage(Damage):
    type: Literal['minecraft:range_dispatch'] = 'minecraft:range_dispatch'
    property: Literal['minecraft:damage'] = 'minecraft:damage'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelRangeDispatchTime(Time):
    type: Literal['minecraft:range_dispatch'] = 'minecraft:range_dispatch'
    property: Literal['minecraft:time'] = 'minecraft:time'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelRangeDispatchUseCycle(UseCycle):
    type: Literal['minecraft:range_dispatch'] = 'minecraft:range_dispatch'
    property: Literal['minecraft:use_cycle'] = 'minecraft:use_cycle'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelRangeDispatchUseDuration(UseDuration):
    type: Literal['minecraft:range_dispatch'] = 'minecraft:range_dispatch'
    property: Literal['minecraft:use_duration'] = 'minecraft:use_duration'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


type ItemModelRangeDispatch = ItemModelRangeDispatchUnknown | ItemModelRangeDispatchCompass | ItemModelRangeDispatchCount | ItemModelRangeDispatchCustomModelData | ItemModelRangeDispatchDamage | ItemModelRangeDispatchTime | ItemModelRangeDispatchUseCycle | ItemModelRangeDispatchUseDuration

@dataclass(kw_only=True)
class ItemModelSelectUnknown(SelectCases[str]):
    type: Literal['minecraft:select'] = 'minecraft:select'
    property: SelectPropertyType
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelSelectBlockState(BlockState):
    type: Literal['minecraft:select'] = 'minecraft:select'
    property: Literal['minecraft:block_state'] = 'minecraft:block_state'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelSelectChargeType(ChargeType):
    type: Literal['minecraft:select'] = 'minecraft:select'
    property: Literal['minecraft:charge_type'] = 'minecraft:charge_type'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelSelectComponent(ComponentStrings):
    type: Literal['minecraft:select'] = 'minecraft:select'
    property: Literal['minecraft:component'] = 'minecraft:component'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelSelectContextDimension(ContextDimension):
    type: Literal['minecraft:select'] = 'minecraft:select'
    property: Literal['minecraft:context_dimension'] = 'minecraft:context_dimension'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelSelectContextEntityType(ContextEntityType):
    type: Literal['minecraft:select'] = 'minecraft:select'
    property: Literal['minecraft:context_entity_type'] = 'minecraft:context_entity_type'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelSelectCustomModelData(CustomModelDataStrings):
    type: Literal['minecraft:select'] = 'minecraft:select'
    property: Literal['minecraft:custom_model_data'] = 'minecraft:custom_model_data'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelSelectDisplayContext(DisplayContext):
    type: Literal['minecraft:select'] = 'minecraft:select'
    property: Literal['minecraft:display_context'] = 'minecraft:display_context'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelSelectLocalTime(LocalTime):
    type: Literal['minecraft:select'] = 'minecraft:select'
    property: Literal['minecraft:local_time'] = 'minecraft:local_time'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelSelectMainHand(MainHand):
    type: Literal['minecraft:select'] = 'minecraft:select'
    property: Literal['minecraft:main_hand'] = 'minecraft:main_hand'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelSelectTrimMaterial(TrimMaterial):
    type: Literal['minecraft:select'] = 'minecraft:select'
    property: Literal['minecraft:trim_material'] = 'minecraft:trim_material'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


type ItemModelSelect = ItemModelSelectUnknown | ItemModelSelectBlockState | ItemModelSelectChargeType | ItemModelSelectComponent | ItemModelSelectContextDimension | ItemModelSelectContextEntityType | ItemModelSelectCustomModelData | ItemModelSelectDisplayContext | ItemModelSelectLocalTime | ItemModelSelectMainHand | ItemModelSelectTrimMaterial

@dataclass(kw_only=True)
class ItemModelSpecial(Special):
    type: Literal['minecraft:special'] = 'minecraft:special'


type ItemModel = ItemModelBundleSelectedItem | ItemModelComposite | ItemModelCondition | ItemModelModel | ItemModelRangeDispatch | ItemModelSelect | ItemModelSpecial


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

