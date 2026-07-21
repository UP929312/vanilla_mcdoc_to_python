# Generated from symbols.json for ::java::assets::texture_meta::PaletteMeta
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.atlas.PaletteRef import PaletteRef


@dataclass(kw_only=True)
class PaletteMeta:
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

