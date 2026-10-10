"""
Generated from symbols.json for ::java::assets::atlas::SpriteSource
Local link to file: generated_symbols/assets/atlas/SpriteSource.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from generated_symbols.assets.atlas.Directory import Directory
from generated_symbols.assets.atlas.Filter import Filter
from generated_symbols.assets.atlas.PalettedPermutations import PalettedPermutations
from generated_symbols.assets.atlas.Single import Single
from generated_symbols.assets.atlas.Unstitch import Unstitch


class SpriteSourceDirectory(Directory):
    type: Literal['minecraft:directory', 'directory'] = 'minecraft:directory'


class SpriteSourceFilter(Filter):
    type: Literal['minecraft:filter', 'filter'] = 'minecraft:filter'


class SpriteSourcePalettedPermutations(PalettedPermutations):
    type: Literal['minecraft:paletted_permutations', 'paletted_permutations'] = 'minecraft:paletted_permutations'


class SpriteSourceSingle(Single):
    type: Literal['minecraft:single', 'single'] = 'minecraft:single'


class SpriteSourceUnstitch(Unstitch):
    type: Literal['minecraft:unstitch', 'unstitch'] = 'minecraft:unstitch'


type SpriteSource = Annotated[
    SpriteSourceDirectory | SpriteSourceFilter | SpriteSourcePalettedPermutations | SpriteSourceSingle | SpriteSourceUnstitch,
    Field(discriminator='type'),
]


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
