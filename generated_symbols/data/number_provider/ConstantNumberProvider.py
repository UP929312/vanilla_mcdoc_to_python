"""
Generated from symbols.json for ::java::data::number_provider::ConstantNumberProvider
Local link to file: generated_symbols/data/number_provider/ConstantNumberProvider.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass


@dataclass(kw_only=True)
class ConstantNumberProvider:
    value: float


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::ConstantNumberProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "value",
                "type": {
                    "kind": "float"
                }
            }
        ]
    }
}

