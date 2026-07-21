# Generated from symbols.json for ::java::assets::texture_meta::NineSlice
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.assets.texture_meta.NineSliceBorder import NineSliceBorder


@dataclass(kw_only=True)
class NineSlice:
    width: Annotated[int, 'Range | Min `1` and above | inclusive']
    height: Annotated[int, 'Range | Min `1` and above | inclusive']
    border: Annotated[int, 'Range | Min `1` and above | inclusive'] | NineSliceBorder
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

