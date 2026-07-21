# Generated from symbols.json for ::java::assets::texture_meta::ColormapTextureMeta
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.assets.texture_meta.MipmapStrategy import MipmapStrategy


@dataclass(kw_only=True)
class ColormapTextureMeta:
    blur: bool | None = None  # Causes the texture to blur when viewed from close up. Defaults to false.
    clamp: bool | None = None  # Causes the texture to stretch instead of tiling in cases where it otherwise would, such as on the shadow. Defaults to false.
    mipmap_strategy: MipmapStrategy | None = None  # Defaults to `auto`.
    alpha_cutoff_bias: Annotated[float, 'Range | `-1`-`1` | both inclusive'] | None = None  # The alpha bias for cutout textures.  Positive values make the texture more opaque at distance. Negative values make the texture more transparent at distance.  Defaults to 0.0


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::texture_meta::ColormapTextureMeta": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Causes the texture to blur when viewed from close up. Defaults to False.",
                "key": "blur",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Causes the texture to stretch instead of tiling in cases where it otherwise would, such as on the shadow. Defaults to False.",
                "key": "clamp",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "desc": "Defaults to `auto`.",
                "key": "mipmap_strategy",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::texture_meta::MipmapStrategy"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "desc": "The alpha bias for cutout textures. \\\nPositive values make the texture more opaque at distance.\nNegative values make the texture more transparent at distance. \\\nDefaults to 0.0",
                "key": "alpha_cutoff_bias",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": -1,
                        "max": 1
                    }
                },
                "optional": True
            }
        ]
    }
}

