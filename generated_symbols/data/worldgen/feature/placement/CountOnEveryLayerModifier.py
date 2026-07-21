# Generated from symbols.json for ::java::data::worldgen::feature::placement::CountOnEveryLayerModifier
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider


@dataclass(kw_only=True)
class CountOnEveryLayerModifier:
    count: IntProvider[Annotated[int, 'Range | `0`-`256` | both inclusive']] | Annotated[int, 'Range | `0`-`256` | both inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::placement::CountOnEveryLayerModifier": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "count",
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
                                "min": 0,
                                "max": 256
                            }
                        }
                    ]
                }
            }
        ]
    }
}

