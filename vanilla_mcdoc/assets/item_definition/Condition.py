"""
Generated from symbols.json for ::java::assets::item_definition::Condition
Local link to file: vanilla_mcdoc/assets/item_definition/Condition.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Literal

from vanilla_mcdoc.assets.item_definition.ComponentFlags import ComponentFlags
from vanilla_mcdoc.assets.item_definition.CustomModelDataFlags import CustomModelDataFlags
from vanilla_mcdoc.assets.item_definition.HasComponent import HasComponent
from vanilla_mcdoc.assets.item_definition.KeybindDown import KeybindDown
from vanilla_mcdoc.assets.item_definition.ViewEntity import ViewEntity
from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.item_definition.ConditionalPropertyType import ConditionalPropertyType
    from vanilla_mcdoc.assets.item_definition.ItemModel import ItemModel
    from vanilla_mcdoc.world.entity.display.Transformation import Transformation


class ConditionUnknown(GeneratedModel):
    property: ConditionalPropertyType
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


class ConditionComponent(ComponentFlags):
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


class ConditionCustomModelData(CustomModelDataFlags):
    property: Literal['minecraft:custom_model_data', 'custom_model_data'] = 'minecraft:custom_model_data'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


class ConditionHasComponent(HasComponent):
    property: Literal['minecraft:has_component', 'has_component'] = 'minecraft:has_component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


class ConditionKeybindDown(KeybindDown):
    property: Literal['minecraft:keybind_down', 'keybind_down'] = 'minecraft:keybind_down'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


class ConditionViewEntity(ViewEntity):
    property: Literal['minecraft:view_entity', 'view_entity'] = 'minecraft:view_entity'
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
