# Generated from symbols.json for ::java::data::worldgen::UniformIntProvider
from dataclasses import dataclass
from typing import Generic, TypeVar


T = TypeVar('T')

@dataclass(kw_only=True)
class UniformIntProvider(Generic[T]):
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

