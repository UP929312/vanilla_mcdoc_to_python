"""
Generated from symbols.json for ::java::assets::atlas::SpriteSource
Local link to file: vanilla_mcdoc/assets/atlas/SpriteSource.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.assets.atlas.Directory import Directory
from vanilla_mcdoc.assets.atlas.Filter import Filter
from vanilla_mcdoc.assets.atlas.PalettedPermutations import PalettedPermutations
from vanilla_mcdoc.assets.atlas.Single import Single
from vanilla_mcdoc.assets.atlas.Unstitch import Unstitch


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
