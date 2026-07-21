# Generated from symbols.json for ::java::data::worldgen::structure::JigsawDistanceLimits
from dataclasses import dataclass
from typing import Annotated, Generic, TypeVar


T = TypeVar('T')

@dataclass(kw_only=True)
class JigsawDistanceLimits(Generic[T]):
    horizontal: T
    vertical: Annotated[int, 'Range | `1`-`4064` | both inclusive'] | None = None  # Defaults to 4064


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure::JigsawDistanceLimits": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "key": "horizontal",
                    "type": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::structure::T"
                    }
                },
                {
                    "kind": "pair",
                    "desc": "Defaults to 4064",
                    "key": "vertical",
                    "type": {
                        "kind": "int",
                        "valueRange": {
                            "kind": 0,
                            "min": 1,
                            "max": 4064
                        }
                    },
                    "optional": True
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::data::worldgen::structure::T"
            }
        ]
    }
}

