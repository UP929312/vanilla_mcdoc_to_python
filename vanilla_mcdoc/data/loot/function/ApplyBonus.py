"""
Generated from symbols.json for ::java::data::loot::function::ApplyBonus
Local link to file: vanilla_mcdoc/data/loot/function/ApplyBonus.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.data.loot.function.BinomialWithBonusCountFormula import BinomialWithBonusCountFormula
from vanilla_mcdoc.data.loot.function.Conditions import Conditions
from vanilla_mcdoc.data.loot.function.UniformBonusFormula import UniformBonusFormula
from vanilla_mcdoc.minecraft_types import IdSpec


class ApplyBonusBinomialWithBonusCount(BinomialWithBonusCountFormula, Conditions):
    enchantment: Annotated[str, IdSpec(registry='enchantment')]
    formula: Literal['minecraft:binomial_with_bonus_count', 'binomial_with_bonus_count'] = 'minecraft:binomial_with_bonus_count'


class ApplyBonusOreDrops(Conditions):
    enchantment: Annotated[str, IdSpec(registry='enchantment')]
    formula: Literal['minecraft:ore_drops', 'ore_drops'] = 'minecraft:ore_drops'


class ApplyBonusUniformBonusCount(Conditions, UniformBonusFormula):
    enchantment: Annotated[str, IdSpec(registry='enchantment')]
    formula: Literal['minecraft:uniform_bonus_count', 'uniform_bonus_count'] = 'minecraft:uniform_bonus_count'


type ApplyBonus = Annotated[
    ApplyBonusBinomialWithBonusCount | ApplyBonusOreDrops | ApplyBonusUniformBonusCount,
    Field(discriminator='formula'),
]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::ApplyBonus": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "enchantment",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "enchantment"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "formula",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::ApplyBonusFormula",
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
                                "formula"
                            ]
                        }
                    ],
                    "registry": "minecraft:apply_bonus_formula"
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::Conditions"
                }
            }
        ]
    }
}
