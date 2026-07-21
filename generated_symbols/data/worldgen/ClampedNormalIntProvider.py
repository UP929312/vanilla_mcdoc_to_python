# Generated from symbols.json for ::java::data::worldgen::ClampedNormalIntProvider
from dataclasses import dataclass
from typing import Generic, TypeVar
from generated_symbols.data.worldgen.UniformIntProvider import UniformIntProvider


T = TypeVar('T')

@dataclass(kw_only=True)
class ClampedNormalIntProvider(UniformIntProvider[T], Generic[T]):
    mean: float
    deviation: float


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::ClampedNormalIntProvider": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "spread",
                    "type": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::data::worldgen::UniformIntProvider"
                        },
                        "typeArgs": [
                            {
                                "kind": "reference",
                                "path": "::java::data::worldgen::T"
                            }
                        ]
                    }
                },
                {
                    "kind": "pair",
                    "key": "mean",
                    "type": {
                        "kind": "float"
                    }
                },
                {
                    "kind": "pair",
                    "key": "deviation",
                    "type": {
                        "kind": "float"
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

