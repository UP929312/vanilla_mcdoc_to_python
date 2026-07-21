# Generated from symbols.json for ::java::data::worldgen::feature::placement::CuboidModifier
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider


@dataclass(kw_only=True)
class CuboidModifier:
    xz_size: IntProvider[Annotated[int, 'Range | `1`-`16` | both inclusive']] | Annotated[int, 'Range | `1`-`16` | both inclusive']
    y_size: IntProvider[Annotated[int, 'Range | `1`-`16` | both inclusive']] | Annotated[int, 'Range | `1`-`16` | both inclusive']
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

