"""
Generated from symbols.json for ::java::util::ExplicitInclusiveRange
Local link to file: vanilla_mcdoc/util/ExplicitInclusiveRange.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


T = TypeVar('T')


class ExplicitInclusiveRange(GeneratedModel, Generic[T]):
    min_inclusive: T
    max_inclusive: T


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::ExplicitInclusiveRange": {
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
}
