"""
Generated from symbols.json for ::java::assets::atlas::PalettedPermutations
Local link to file: generated_symbols/assets/atlas/PalettedPermutations.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.assets.atlas.PaletteTexture import PaletteTexture


@dataclass(kw_only=True)
class PalettedPermutations:
    textures: list[Annotated[str, IdSpec(registry='texture')]]
    palette_key: PaletteTexture
    permutations: dict[str, PaletteTexture]
    separator: str | None = None  # Value to use when joining the texture and permutation names to produce the sprite name. Defaults to `_`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::atlas::PalettedPermutations": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "textures",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string",
                        "attributes": [
                            {
                                "name": "id",
                                "value": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "texture"
                                    }
                                }
                            }
                        ]
                    }
                }
            },
            {
                "kind": "pair",
                "key": "palette_key",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::atlas::PaletteTexture"
                }
            },
            {
                "kind": "pair",
                "key": "permutations",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "permutation",
                                        "value": {
                                            "kind": "tree",
                                            "values": {
                                                "definition": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "boolean",
                                                        "value": True
                                                    }
                                                }
                                            }
                                        }
                                    }
                                ]
                            },
                            "type": {
                                "kind": "reference",
                                "path": "::java::assets::atlas::PaletteTexture"
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Value to use when joining the texture and permutation names to produce the sprite name.\nDefaults to `_`.",
                "key": "separator",
                "type": {
                    "kind": "string"
                },
                "optional": True
            }
        ]
    }
}

