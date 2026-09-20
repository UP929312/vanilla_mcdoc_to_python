"""
Generated from symbols.json for ::java::assets::texture_meta::PaletteMeta
Local link to file: generated_symbols/assets/texture_meta/PaletteMeta.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.assets.atlas.PaletteRef import PaletteRef


class PaletteMeta(GeneratedModel):
    base_palette: PaletteRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::texture_meta::PaletteMeta": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "base_palette",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::atlas::PaletteRef"
                }
            }
        ]
    }
}

