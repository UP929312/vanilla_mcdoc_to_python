# Generated from symbols.json for ::java::util::InclusiveRange
from dataclasses import dataclass
from typing import Generic, TypeVar


T = TypeVar('T')

@dataclass(kw_only=True)
class InclusiveRange(Generic[T]):
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

