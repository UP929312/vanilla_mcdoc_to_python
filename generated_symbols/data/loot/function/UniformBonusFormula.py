# Generated from symbols.json for ::java::data::loot::function::UniformBonusFormula
from dataclasses import dataclass
from typing import Any


@dataclass(kw_only=True)
class UniformBonusFormula:
    parameters: Any


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

