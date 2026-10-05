"""
Generated from symbols.json for ::java::data::number_provider::ConstantValue
Local link to file: generated_symbols/data/number_provider/ConstantValue.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from generated_symbols.base import GeneratedModel


V = TypeVar('V')

class ConstantValue(GeneratedModel, Generic[V]):
    value: V


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::ConstantValue": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "key": "value",
                    "type": {
                        "kind": "reference",
                        "path": "::java::data::number_provider::V"
                    }
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::data::number_provider::V"
            }
        ]
    }
}

