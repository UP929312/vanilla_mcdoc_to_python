"""
Generated from symbols.json for ::java::data::number_provider::PowerProvider
Local link to file: vanilla_mcdoc/data/number_provider/PowerProvider.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


T = TypeVar('T')


class PowerProvider(GeneratedModel, Generic[T]):
    base: T
    exponent: T


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::PowerProvider": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "key": "base",
                    "type": {
                        "kind": "reference",
                        "path": "::java::data::number_provider::T"
                    }
                },
                {
                    "kind": "pair",
                    "key": "exponent",
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
