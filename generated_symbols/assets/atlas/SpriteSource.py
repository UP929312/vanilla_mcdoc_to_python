"""
Generated from symbols.json for ::java::assets::atlas::SpriteSource
Local link to file: generated_symbols/assets/atlas/SpriteSource.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.assets.atlas.FilterPattern import FilterPattern
    from generated_symbols.assets.atlas.PaletteTexture import PaletteTexture
    from generated_symbols.assets.atlas.UnstitchRegion import UnstitchRegion


@dataclass(kw_only=True)
class SpriteSourceDirectory:
    type: Literal['minecraft:directory']
    source: str  # Directory of texture locations to include, relative to the `textures` folder, not including the trailing `/`.
    prefix: str  # The sprite name prefix, usually ending with `/`.


@dataclass(kw_only=True)
class SpriteSourceFilter:
    type: Literal['minecraft:filter']
    pattern: FilterPattern  # Pattern to remove sprite identifiers already in the atlas. The order of sprite sources is important.


@dataclass(kw_only=True)
class SpriteSourcePalettedPermutations:
    type: Literal['minecraft:paletted_permutations']
    textures: list[Annotated[str, IdSpec(registry='texture')]]
    palette_key: PaletteTexture
    permutations: dict[str, PaletteTexture]
    separator: str | None = None  # Value to use when joining the texture and permutation names to produce the sprite name. Defaults to `_`.


@dataclass(kw_only=True)
class SpriteSourceSingle:
    type: Literal['minecraft:single']
    resource: Annotated[str, IdSpec(registry='texture')]  # A single texture location of the source.
    sprite: Annotated[str, IdSpec(registry='texture', definition=True)] | None = None  # The identifier of the sprite that can referenced. If not specified, matches `resource`.


@dataclass(kw_only=True)
class SpriteSourceUnstitch:
    type: Literal['minecraft:unstitch']
    resource: Annotated[str, IdSpec(registry='texture')]
    divisor_x: float | None = None  # If set to the resource width, regions will use pixel coordinates.
    divisor_y: float | None = None  # If set to the resource height, regions will use pixel coordinates.
    regions: list[UnstitchRegion]


type SpriteSource = SpriteSourceDirectory | SpriteSourceFilter | SpriteSourcePalettedPermutations | SpriteSourceSingle | SpriteSourceUnstitch


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::atlas::SpriteSource": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::assets::atlas::SpriteSourceType",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.5"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::assets::atlas::SpriteSourceType",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.5"
                                        }
                                    }
                                },
                                {
                                    "name": "id"
                                }
                            ]
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:sprite_source"
                }
            }
        ]
    }
}

