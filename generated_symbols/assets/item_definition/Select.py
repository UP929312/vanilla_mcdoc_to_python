"""
Generated from symbols.json for ::java::assets::item_definition::Select
Local link to file: generated_symbols/assets/item_definition/Select.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from generated_symbols.assets.item_definition.BlockState import BlockState
from generated_symbols.assets.item_definition.ChargeType import ChargeType
from generated_symbols.assets.item_definition.ComponentStrings import ComponentStrings
from generated_symbols.assets.item_definition.ContextDimension import ContextDimension
from generated_symbols.assets.item_definition.ContextEntityType import ContextEntityType
from generated_symbols.assets.item_definition.CustomModelDataStrings import CustomModelDataStrings
from generated_symbols.assets.item_definition.DisplayContext import DisplayContext
from generated_symbols.assets.item_definition.LocalTime import LocalTime
from generated_symbols.assets.item_definition.MainHand import MainHand
from generated_symbols.assets.item_definition.SelectCases import SelectCases
from generated_symbols.assets.item_definition.TrimMaterial import TrimMaterial

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.ItemModel import ItemModel
    from generated_symbols.assets.item_definition.SelectPropertyType import SelectPropertyType
    from generated_symbols.world.entity.display.Transformation import Transformation


@dataclass(kw_only=True)
class SelectUnknown(SelectCases[str]):
    property: SelectPropertyType
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class SelectBlockState(BlockState):
    property: Literal['minecraft:block_state'] = 'minecraft:block_state'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class SelectChargeType(ChargeType):
    property: Literal['minecraft:charge_type'] = 'minecraft:charge_type'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class SelectComponent(ComponentStrings):
    property: Literal['minecraft:component'] = 'minecraft:component'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class SelectContextDimension(ContextDimension):
    property: Literal['minecraft:context_dimension'] = 'minecraft:context_dimension'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class SelectContextEntityType(ContextEntityType):
    property: Literal['minecraft:context_entity_type'] = 'minecraft:context_entity_type'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class SelectCustomModelData(CustomModelDataStrings):
    property: Literal['minecraft:custom_model_data'] = 'minecraft:custom_model_data'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class SelectDisplayContext(DisplayContext):
    property: Literal['minecraft:display_context'] = 'minecraft:display_context'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class SelectLocalTime(LocalTime):
    property: Literal['minecraft:local_time'] = 'minecraft:local_time'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class SelectMainHand(MainHand):
    property: Literal['minecraft:main_hand'] = 'minecraft:main_hand'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class SelectTrimMaterial(TrimMaterial):
    property: Literal['minecraft:trim_material'] = 'minecraft:trim_material'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


type Select = SelectUnknown | SelectBlockState | SelectChargeType | SelectComponent | SelectContextDimension | SelectContextEntityType | SelectCustomModelData | SelectDisplayContext | SelectLocalTime | SelectMainHand | SelectTrimMaterial


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::Select": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "property",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::SelectPropertyType",
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
                    "registry": "minecraft:select_item_property"
                }
            },
            {
                "kind": "pair",
                "desc": "Item model to render if none of the cases matched the value.",
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

