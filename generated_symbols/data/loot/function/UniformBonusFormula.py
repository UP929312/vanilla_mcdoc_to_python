# Generated from symbols.json for ::java::data::loot::function::UniformBonusFormula
from dataclasses import dataclass


@dataclass(kw_only=True)
class ParametersStruct:
    bonusMultiplier: int


@dataclass(kw_only=True)
class UniformBonusFormula:
    parameters: ParametersStruct


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::UniformBonusFormula": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "parameters",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "bonusMultiplier",
                            "type": {
                                "kind": "int"
                            }
                        }
                    ]
                }
            }
        ]
    }
}

