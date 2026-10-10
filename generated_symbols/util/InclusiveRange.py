"""
Generated from symbols.json for ::java::util::InclusiveRange
Local link to file: generated_symbols/util/InclusiveRange.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from generated_symbols.base import GeneratedModel


T = TypeVar('T')


class InclusiveRange(GeneratedModel, Generic[T]):
    min_inclusive: T
    max_inclusive: T


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::InclusiveRange": {
        "kind": "template",
        "child": {
            "kind": "union",
            "members": [
                {
                    "kind": "reference",
                    "path": "::java::util::T"
                },
                {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::util::T"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 2,
                        "max": 2
                    }
                },
                {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "min_inclusive",
                            "type": {
                                "kind": "reference",
                                "path": "::java::util::T"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "max_inclusive",
                            "type": {
                                "kind": "reference",
                                "path": "::java::util::T"
                            }
                        }
                    ]
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::util::T"
            }
        ]
    }
}
