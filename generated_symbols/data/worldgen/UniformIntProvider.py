"""
Generated from symbols.json for ::java::data::worldgen::UniformIntProvider
Local link to file: generated_symbols/data/worldgen/UniformIntProvider.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from generated_symbols.base import GeneratedModel


T = TypeVar('T')


class UniformIntProvider(GeneratedModel, Generic[T]):
    min_inclusive: T
    max_inclusive: T


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::UniformIntProvider": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "key": "min_inclusive",
                    "type": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::T"
                    }
                },
                {
                    "kind": "pair",
                    "key": "max_inclusive",
                    "type": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::T"
                    }
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::data::worldgen::T"
            }
        ]
    }
}
