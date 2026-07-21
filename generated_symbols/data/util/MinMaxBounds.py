# Generated from symbols.json for ::java::data::util::MinMaxBounds
from dataclasses import dataclass
from typing import Generic, TypeVar


T = TypeVar('T')

@dataclass(kw_only=True)
class MinMaxBounds(Generic[T]):
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

