"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::CountOnEveryLayerModifier
Local link to file: generated_symbols/data/worldgen/feature/placement/CountOnEveryLayerModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider


class CountOnEveryLayerModifier(GeneratedModel):
    count: IntProvider[Annotated[int, Field(ge=0, le=256)]] | Annotated[int, Field(ge=0, le=256)]


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

