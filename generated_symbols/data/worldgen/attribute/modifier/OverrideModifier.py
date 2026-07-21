# Generated from symbols.json for ::java::data::worldgen::attribute::modifier::OverrideModifier
from dataclasses import dataclass
from typing import Generic, TypeVar


T = TypeVar('T')

@dataclass(kw_only=True)
class OverrideModifier(Generic[T]):
    modifier: str
    argument: T


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::modifier::OverrideModifier": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "key": "modifier",
                    "type": {
                        "kind": "literal",
                        "value": {
                            "kind": "string",
                            "value": "override"
                        }
                    }
                },
                {
                    "kind": "pair",
                    "key": "argument",
                    "type": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::attribute::modifier::T"
                    }
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::data::worldgen::attribute::modifier::T"
            }
        ]
    }
}

