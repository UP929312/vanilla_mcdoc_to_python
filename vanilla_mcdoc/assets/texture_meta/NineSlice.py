"""
Generated from symbols.json for ::java::assets::texture_meta::NineSlice
Local link to file: vanilla_mcdoc/assets/texture_meta/NineSlice.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.texture_meta.NineSliceBorder import NineSliceBorder


class NineSlice(GeneratedModel):
    width: Annotated[int, Field(ge=1)]
    height: Annotated[int, Field(ge=1)]
    border: Annotated[int, Field(ge=1)] | NineSliceBorder
    stretch_inner: bool | None = None  # Defaults to `false`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::texture_meta::NineSlice": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "width",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            },
            {
                "kind": "pair",
                "key": "height",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            },
            {
                "kind": "pair",
                "key": "border",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": 1
                            }
                        },
                        {
                            "kind": "reference",
                            "path": "::java::assets::texture_meta::NineSliceBorder"
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Defaults to `False`.",
                "key": "stretch_inner",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}
