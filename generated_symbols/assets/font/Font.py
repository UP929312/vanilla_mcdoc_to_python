# Generated from symbols.json for ::java::assets::font::Font
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.font.GlyphProvider import GlyphProvider


@dataclass(kw_only=True)
class Font:
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

