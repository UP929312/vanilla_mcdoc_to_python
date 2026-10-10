"""
Generated from symbols.json for ::java::world::component::DataComponentPredicate
Local link to file: vanilla_mcdoc/world/component/DataComponentPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.predicate.EnchantmentPredicate import EnchantmentPredicate
    from vanilla_mcdoc.world.component.CustomData import CustomData
    from vanilla_mcdoc.world.component.predicate.AttributeModifiersPredicate import AttributeModifiersPredicate
    from vanilla_mcdoc.world.component.predicate.BundleContentsPredicate import BundleContentsPredicate
    from vanilla_mcdoc.world.component.predicate.ContainerPredicate import ContainerPredicate
    from vanilla_mcdoc.world.component.predicate.FireworkExplosionPredicate import FireworkExplosionPredicate
    from vanilla_mcdoc.world.component.predicate.FireworksPredicate import FireworksPredicate
    from vanilla_mcdoc.world.component.predicate.ItemDamagePredicate import ItemDamagePredicate
    from vanilla_mcdoc.world.component.predicate.JukeboxPlayablePredicate import JukeboxPlayablePredicate
    from vanilla_mcdoc.world.component.predicate.PotionsPredicate import PotionsPredicate
    from vanilla_mcdoc.world.component.predicate.TrimPredicate import TrimPredicate
    from vanilla_mcdoc.world.component.predicate.WritableBookPredicate import WritableBookPredicate
    from vanilla_mcdoc.world.component.predicate.WrittenBookPredicate import WrittenBookPredicate


class DataComponentPredicateValueStructDataComponentExistencePredicateUnknown(GeneratedModel):
    pass


type DataComponentPredicate = dict[Annotated[str, IdSpec(registry='data_component_type')], None | AttributeModifiersPredicate | BundleContentsPredicate | ContainerPredicate | CustomData | ItemDamagePredicate | list[EnchantmentPredicate] | FireworkExplosionPredicate | FireworksPredicate | JukeboxPlayablePredicate | PotionsPredicate | TrimPredicate | Annotated[str, IdSpec(registry='villager_type', tags='allowed')] | list[Annotated[str, IdSpec(registry='villager_type')]] | WritableBookPredicate | WrittenBookPredicate | DataComponentPredicateValueStructDataComponentExistencePredicateUnknown | None]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::DataComponentPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
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
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.11"
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
                                            "value": "1.21.11"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "data_component_type"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                },
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "dispatcher",
                            "parallelIndices": [
                                {
                                    "kind": "dynamic",
                                    "accessor": [
                                        {
                                            "keyword": "key"
                                        }
                                    ]
                                }
                            ],
                            "registry": "minecraft:data_component_predicate"
                        },
                        {
                            "kind": "dispatcher",
                            "parallelIndices": [
                                {
                                    "kind": "dynamic",
                                    "accessor": [
                                        {
                                            "keyword": "key"
                                        }
                                    ]
                                }
                            ],
                            "registry": "minecraft:data_component_existence_predicate",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.11"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }
}
