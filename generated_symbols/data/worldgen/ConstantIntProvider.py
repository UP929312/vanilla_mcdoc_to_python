# Generated from symbols.json for ::java::data::worldgen::ConstantIntProvider
from dataclasses import dataclass
from typing import Generic, TypeVar


T = TypeVar('T')

@dataclass(kw_only=True)
class ConstantIntProvider(Generic[T]):
    value: T


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::ConstantIntProvider": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "key": "value",
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

