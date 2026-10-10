"""
Generated from symbols.json for ::java::data::util::MinMaxBounds
Local link to file: generated_symbols/data/util/MinMaxBounds.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from generated_symbols.base import GeneratedModel


T = TypeVar('T')


class MinMaxBounds(GeneratedModel, Generic[T]):
    min: T | None = None
    max: T | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::util::MinMaxBounds": {
        "kind": "template",
        "child": {
            "kind": "union",
            "members": [
                {
                    "kind": "reference",
                    "path": "::java::data::util::T"
                },
                {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "min",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::util::T"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "max",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::util::T"
                            },
                            "optional": True
                        }
                    ]
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::data::util::T"
            }
        ]
    }
}
