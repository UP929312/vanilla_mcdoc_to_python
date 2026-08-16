"""
Generated from symbols.json for ::java::assets::font::Font
Local link to file: generated_symbols/assets/font/Font.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from generated_symbols.assets.font.GlyphProvider import GlyphProvider


@dataclass(kw_only=True)
class Font:
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

