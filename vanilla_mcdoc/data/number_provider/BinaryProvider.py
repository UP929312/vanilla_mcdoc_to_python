"""
Generated from symbols.json for ::java::data::number_provider::BinaryProvider
Local link to file: generated_symbols/data/number_provider/BinaryProvider.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from generated_symbols.base import GeneratedModel


T = TypeVar('T')


class BinaryProvider(GeneratedModel, Generic[T]):
    left: T
    right: T


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::BinaryProvider": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "key": "left",
                    "type": {
                        "kind": "reference",
                        "path": "::java::data::number_provider::T"
                    }
                },
                {
                    "kind": "pair",
                    "key": "right",
                    "type": {
                        "kind": "reference",
                        "path": "::java::data::number_provider::T"
                    }
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::data::number_provider::T"
            }
        ]
    }
}
