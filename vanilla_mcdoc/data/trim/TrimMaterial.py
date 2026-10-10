"""
Generated from symbols.json for ::java::data::trim::TrimMaterial
Local link to file: vanilla_mcdoc/data/trim/TrimMaterial.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.atlas.PaletteRef import PaletteRef
    from vanilla_mcdoc.util.text.Text import Text


class TrimMaterial(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'trim_material'

    palette_id: PaletteRef  # Palette ID which will be used in the resource pack.
    description: Text  # Text displayed in the item tooltip.
