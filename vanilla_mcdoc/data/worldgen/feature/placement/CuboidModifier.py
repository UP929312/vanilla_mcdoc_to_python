"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::CuboidModifier
Local link to file: vanilla_mcdoc/data/worldgen/feature/placement/CuboidModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider


class CuboidModifier(GeneratedModel):
    xz_size: IntProvider[Annotated[int, Field(ge=1, le=16)]] | Annotated[int, Field(ge=1, le=16)]
    y_size: IntProvider[Annotated[int, Field(ge=1, le=16)]] | Annotated[int, Field(ge=1, le=16)]
    include_interior: bool | None = None  # Defaults to `true`.
    include_edges: bool | None = None  # Defaults to `true`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::placement::CuboidModifier": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "xz_size",
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
                                "min": 1,
                                "max": 16
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "y_size",
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
                                "min": 1,
                                "max": 16
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Defaults to `True`.",
                "key": "include_interior",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Defaults to `True`.",
                "key": "include_edges",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}
