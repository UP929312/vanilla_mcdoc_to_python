# Generated from symbols.json for ::java::assets::item_definition::ComponentFlags
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.EnchantmentPredicate import EnchantmentPredicate
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


@dataclass(kw_only=True)
class ComponentFlags:
    predicate: Annotated[str, IdSpec(registry='data_component_predicate_type')]  # The component predicate to check.
    value: None | AttributeModifiersPredicate | BundleContentsPredicate | ContainerPredicate | CustomData | ItemDamagePredicate | list[EnchantmentPredicate] | FireworkExplosionPredicate | FireworksPredicate | JukeboxPlayablePredicate | PotionsPredicate | TrimPredicate | Annotated[str, IdSpec(registry='villager_type', tags='allowed')] | list[Annotated[str, IdSpec(registry='villager_type')]] | WritableBookPredicate | WrittenBookPredicate  # The predicate-specific value.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::ComponentFlags": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The component predicate to check.",
                "key": "predicate",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.5"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "item_sub_predicate_type"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.5"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "data_component_predicate_type"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "The predicate-specific value.",
                "key": "value",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "predicate"
                            ]
                        }
                    ],
                    "registry": "minecraft:data_component_predicate"
                }
            }
        ]
    }
}

