"""
Generated from symbols.json for ::java::data::loot::function::UniformBonusFormula
Local link to file: vanilla_mcdoc/data/loot/function/UniformBonusFormula.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class ParametersStruct(GeneratedModel):
    bonusMultiplier: int


class UniformBonusFormula(GeneratedModel):
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
