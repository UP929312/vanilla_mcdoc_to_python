"""
Generated from symbols.json for ::java::data::number_provider::legacy::ConstantNumberProvider
Local link to file: generated_symbols/data/number_provider/legacy/ConstantNumberProvider.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel


class ConstantNumberProvider(GeneratedModel):
    value: float


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::legacy::ConstantNumberProvider": {
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
