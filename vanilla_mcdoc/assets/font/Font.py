"""
Generated from symbols.json for ::java::assets::font::Font
Local link to file: generated_symbols/assets/font/Font.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.assets.font.GlyphProvider import GlyphProvider


class Font(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'font'

    providers: list[GlyphProvider]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::font::Font": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "providers",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::assets::font::GlyphProvider"
                    }
                }
            }
        ]
    }
}
