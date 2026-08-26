"""
Generated from symbols.json for ::java::data::loot::function::ApplyBonus
Local link to file: generated_symbols/data/loot/function/ApplyBonus.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated, Literal

from generated_symbols.data.loot.function.BinomialWithBonusCountFormula import BinomialWithBonusCountFormula
from generated_symbols.data.loot.function.Conditions import Conditions
from generated_symbols.data.loot.function.UniformBonusFormula import UniformBonusFormula
from minecraft_registry import IdSpec


@dataclass(kw_only=True)
class ApplyBonusBinomialWithBonusCount(BinomialWithBonusCountFormula, Conditions):
    enchantment: Annotated[str, IdSpec(registry='enchantment')]
    formula: Literal['minecraft:binomial_with_bonus_count'] = 'minecraft:binomial_with_bonus_count'


@dataclass(kw_only=True)
class ApplyBonusOreDrops(Conditions):
    enchantment: Annotated[str, IdSpec(registry='enchantment')]
    formula: Literal['minecraft:ore_drops'] = 'minecraft:ore_drops'


@dataclass(kw_only=True)
class ApplyBonusUniformBonusCount(Conditions, UniformBonusFormula):
    enchantment: Annotated[str, IdSpec(registry='enchantment')]
    formula: Literal['minecraft:uniform_bonus_count'] = 'minecraft:uniform_bonus_count'


type ApplyBonus = ApplyBonusBinomialWithBonusCount | ApplyBonusOreDrops | ApplyBonusUniformBonusCount


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

