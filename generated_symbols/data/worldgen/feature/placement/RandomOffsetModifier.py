# Generated from symbols.json for ::java::data::worldgen::feature::placement::RandomOffsetModifier
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider


@dataclass(kw_only=True)
class RandomOffsetModifier:
    xz_spread: IntProvider[Annotated[int, 'Range | `-16`-`16` | both inclusive']] | Annotated[int, 'Range | `-16`-`16` | both inclusive']
    y_spread: IntProvider[Annotated[int, 'Range | `-16`-`16` | both inclusive']] | Annotated[int, 'Range | `-16`-`16` | both inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::placement::RandomOffsetModifier": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "xz_spread",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::IntProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": -16,
                                "max": 16
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "y_spread",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::IntProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": -16,
                                "max": 16
                            }
                        }
                    ]
                }
            }
        ]
    }
}

