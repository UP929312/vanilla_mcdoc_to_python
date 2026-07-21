# Generated from symbols.json for ::java::util::ExplicitInclusiveRange
from dataclasses import dataclass
from typing import Generic, TypeVar


T = TypeVar('T')

@dataclass(kw_only=True)
class ExplicitInclusiveRange(Generic[T]):
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

