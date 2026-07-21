# Generated from symbols.json for ::java::data::loot::function::ApplyBonus
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from generated_symbols.data.loot.function.ApplyBonusFormula import ApplyBonusFormula


@dataclass(kw_only=True)
class ApplyBonus(Conditions):
    enchantment: str
    formula: ApplyBonusFormula


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

