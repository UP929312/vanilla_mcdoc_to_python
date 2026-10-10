"""
Generated from symbols.json for ::java::data::loot::function::UniformBonusFormula
Local link to file: generated_symbols/data/loot/function/UniformBonusFormula.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel


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
