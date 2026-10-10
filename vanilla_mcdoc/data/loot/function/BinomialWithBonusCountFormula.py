"""
Generated from symbols.json for ::java::data::loot::function::BinomialWithBonusCountFormula
Local link to file: generated_symbols/data/loot/function/BinomialWithBonusCountFormula.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel


class ParametersStruct(GeneratedModel):
    extra: int
    probability: Annotated[float, Field(ge=0, le=1)]


class BinomialWithBonusCountFormula(GeneratedModel):
    parameters: ParametersStruct


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::BinomialWithBonusCountFormula": {
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
                            "key": "extra",
                            "type": {
                                "kind": "int"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "probability",
                            "type": {
                                "kind": "float",
                                "valueRange": {
                                    "kind": 0,
                                    "min": 0,
                                    "max": 1
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}
