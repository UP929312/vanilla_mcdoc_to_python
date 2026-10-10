"""
Generated from symbols.json for ::java::assets::texture_meta::PaletteMeta
Local link to file: vanilla_mcdoc/assets/texture_meta/PaletteMeta.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.atlas.PaletteRef import PaletteRef


class PaletteMeta(GeneratedModel):
    base_palette: PaletteRef
