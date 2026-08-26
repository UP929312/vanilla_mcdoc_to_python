"""
Generated from symbols.json for ::java::assets::item_definition::Condition
Local link to file: generated_symbols/assets/item_definition/Condition.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from generated_symbols.assets.item_definition.ComponentFlags import ComponentFlags
from generated_symbols.assets.item_definition.CustomModelDataFlags import CustomModelDataFlags
from generated_symbols.assets.item_definition.HasComponent import HasComponent
from generated_symbols.assets.item_definition.KeybindDown import KeybindDown
from generated_symbols.assets.item_definition.ViewEntity import ViewEntity

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.ConditionalPropertyType import ConditionalPropertyType
    from generated_symbols.assets.item_definition.ItemModel import ItemModel
    from generated_symbols.world.entity.display.Transformation import Transformation


@dataclass(kw_only=True)
class ConditionUnknown:
    property: ConditionalPropertyType
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ConditionComponent(ComponentFlags):
    property: Literal['minecraft:component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ConditionCustomModelData(CustomModelDataFlags):
    property: Literal['minecraft:custom_model_data'] = 'minecraft:custom_model_data'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ConditionHasComponent(HasComponent):
    property: Literal['minecraft:has_component'] = 'minecraft:has_component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ConditionKeybindDown(KeybindDown):
    property: Literal['minecraft:keybind_down'] = 'minecraft:keybind_down'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ConditionViewEntity(ViewEntity):
    property: Literal['minecraft:view_entity'] = 'minecraft:view_entity'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


type Condition = ConditionUnknown | ConditionComponent | ConditionCustomModelData | ConditionHasComponent | ConditionKeybindDown | ConditionViewEntity


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::Condition": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "property",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::ConditionalPropertyType",
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
                    "registry": "minecraft:conditional_item_property"
                }
            },
            {
                "kind": "pair",
                "key": "on_True",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::ItemModel"
                }
            },
            {
                "kind": "pair",
                "key": "on_False",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::ItemModel"
                }
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

