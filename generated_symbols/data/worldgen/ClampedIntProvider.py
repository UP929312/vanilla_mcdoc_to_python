# Generated from symbols.json for ::java::data::worldgen::ClampedIntProvider
from dataclasses import dataclass
from typing import TYPE_CHECKING, Generic, TypeVar

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider


T = TypeVar('T')

@dataclass(kw_only=True)
class ClampedIntProvider(Generic[T]):
    min_inclusive: T
    max_inclusive: T
    source: IntProvider[int] | int


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::ClampedIntProvider": {
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
                },
                {
                    "kind": "pair",
                    "key": "source",
                    "type": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::data::worldgen::IntProvider"
                        },
                        "typeArgs": [
                            {
                                "kind": "int"
                            }
                        ]
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

