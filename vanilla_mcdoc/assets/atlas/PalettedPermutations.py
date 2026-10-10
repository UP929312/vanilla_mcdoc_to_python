"""
Generated from symbols.json for ::java::assets::atlas::PalettedPermutations
Local link to file: vanilla_mcdoc/assets/atlas/PalettedPermutations.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.atlas.PaletteTexture import PaletteTexture


class PalettedPermutations(GeneratedModel):
    textures: list[Annotated[str, IdSpec(registry='texture')]]
    palette_key: PaletteTexture
    permutations: dict[str, PaletteTexture]
    separator: str | None = None  # Value to use when joining the texture and permutation names to produce the sprite name. Defaults to `_`.
