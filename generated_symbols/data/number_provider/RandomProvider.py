"""
Generated from symbols.json for ::java::data::number_provider::RandomProvider
Local link to file: generated_symbols/data/number_provider/RandomProvider.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from generated_symbols.base import GeneratedModel


T = TypeVar('T')

class RandomProvider(GeneratedModel, Generic[T]):
    min: T
    max: T


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::RandomProvider": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "key": "min",
                    "type": {
                        "kind": "reference",
                        "path": "::java::data::number_provider::T"
                    }
                },
                {
                    "kind": "pair",
                    "key": "max",
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

