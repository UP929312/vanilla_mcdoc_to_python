"""
Generated from symbols.json for ::java::data::loot::function::BinomialWithBonusCountFormula
Local link to file: generated_symbols/data/loot/function/BinomialWithBonusCountFormula.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class ParametersStruct:
    extra: int
    probability: Annotated[float, 'Range | `0`-`1` | both inclusive']


@dataclass(kw_only=True)
class BinomialWithBonusCountFormula:
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

