"""
Generated from symbols.json for ::java::assets::item_definition::Condition
Local link to file: generated_symbols/assets/item_definition/Condition.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.ConditionalPropertyType import ConditionalPropertyType
    from generated_symbols.assets.item_definition.ItemModel import ItemModel
    from generated_symbols.data.advancement.predicate.EnchantmentPredicate import EnchantmentPredicate
    from generated_symbols.util.text.Keybind import Keybind
    from generated_symbols.world.component.CustomData import CustomData
    from generated_symbols.world.component.predicate.AttributeModifiersPredicate import AttributeModifiersPredicate
    from generated_symbols.world.component.predicate.BundleContentsPredicate import BundleContentsPredicate
    from generated_symbols.world.component.predicate.ContainerPredicate import ContainerPredicate
    from generated_symbols.world.component.predicate.FireworkExplosionPredicate import FireworkExplosionPredicate
    from generated_symbols.world.component.predicate.FireworksPredicate import FireworksPredicate
    from generated_symbols.world.component.predicate.ItemDamagePredicate import ItemDamagePredicate
    from generated_symbols.world.component.predicate.JukeboxPlayablePredicate import JukeboxPlayablePredicate
    from generated_symbols.world.component.predicate.PotionsPredicate import PotionsPredicate
    from generated_symbols.world.component.predicate.TrimPredicate import TrimPredicate
    from generated_symbols.world.component.predicate.WritableBookPredicate import WritableBookPredicate
    from generated_symbols.world.component.predicate.WrittenBookPredicate import WrittenBookPredicate
    from generated_symbols.world.entity.display.Transformation import Transformation


@dataclass(kw_only=True)
class ConditionUnknown:
    property: ConditionalPropertyType
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ConditionComponent:
    property: Literal['minecraft:component']
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Annotated[str, IdSpec(registry='data_component_predicate_type')]  # The component predicate to check.
    value: None | AttributeModifiersPredicate | BundleContentsPredicate | ContainerPredicate | CustomData | ItemDamagePredicate | list[EnchantmentPredicate] | FireworkExplosionPredicate | FireworksPredicate | JukeboxPlayablePredicate | PotionsPredicate | TrimPredicate | Annotated[str, IdSpec(registry='villager_type', tags='allowed')] | list[Annotated[str, IdSpec(registry='villager_type')]] | WritableBookPredicate | WrittenBookPredicate  # The predicate-specific value.


@dataclass(kw_only=True)
class ConditionCustomModelData:
    property: Literal['minecraft:custom_model_data']
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    index: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The index of the `flags` list in the `custom_model_data` component. Defaults to 0.


@dataclass(kw_only=True)
class ConditionHasComponent:
    property: Literal['minecraft:has_component']
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    component: Annotated[str, IdSpec(registry='data_component_type')]
    ignore_default: bool | None = None  # Whether the default components should be handled as "no component". Defaults to false.


@dataclass(kw_only=True)
class ConditionKeybindDown:
    property: Literal['minecraft:keybind_down']
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    keybind: Keybind  # The keybind ID to check for.


@dataclass(kw_only=True)
class ConditionViewEntity:
    property: Literal['minecraft:view_entity']
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

