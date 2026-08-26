"""
Generated from symbols.json for ::java::assets::atlas::SpriteSource
Local link to file: generated_symbols/assets/atlas/SpriteSource.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

from generated_symbols.assets.atlas.Directory import Directory
from generated_symbols.assets.atlas.Filter import Filter
from generated_symbols.assets.atlas.PalettedPermutations import PalettedPermutations
from generated_symbols.assets.atlas.Single import Single
from generated_symbols.assets.atlas.Unstitch import Unstitch


@dataclass(kw_only=True)
class SpriteSourceDirectory(Directory):
    type: Literal['minecraft:directory']


@dataclass(kw_only=True)
class SpriteSourceFilter(Filter):
    type: Literal['minecraft:filter']


@dataclass(kw_only=True)
class SpriteSourcePalettedPermutations(PalettedPermutations):
    type: Literal['minecraft:paletted_permutations']


@dataclass(kw_only=True)
class SpriteSourceSingle(Single):
    type: Literal['minecraft:single']


@dataclass(kw_only=True)
class SpriteSourceUnstitch(Unstitch):
    type: Literal['minecraft:unstitch']


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

