"""
Generated from symbols.json for ::java::assets::font::GlyphProvider
Local link to file: generated_symbols/assets/font/GlyphProvider.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from generated_symbols.assets.font.BitmapProvider import BitmapProvider
from generated_symbols.assets.font.ReferenceProvider import ReferenceProvider
from generated_symbols.assets.font.SpaceProvider import SpaceProvider
from generated_symbols.assets.font.TtfProvider import TtfProvider
from generated_symbols.assets.font.UnihexProvider import UnihexProvider

if TYPE_CHECKING:
    from generated_symbols.assets.font.FontOption import FontOption


@dataclass(kw_only=True)
class GlyphProviderBitmap(BitmapProvider):
    type: Literal['minecraft:bitmap']
    filter: dict[FontOption, bool] | None = None


@dataclass(kw_only=True)
class GlyphProviderReference(ReferenceProvider):
    type: Literal['minecraft:reference']
    filter: dict[FontOption, bool] | None = None


@dataclass(kw_only=True)
class GlyphProviderSpace(SpaceProvider):
    type: Literal['minecraft:space']
    filter: dict[FontOption, bool] | None = None


@dataclass(kw_only=True)
class GlyphProviderTtf(TtfProvider):
    type: Literal['minecraft:ttf']
    filter: dict[FontOption, bool] | None = None


@dataclass(kw_only=True)
class GlyphProviderUnihex(UnihexProvider):
    type: Literal['minecraft:unihex']
    filter: dict[FontOption, bool] | None = None


type GlyphProvider = GlyphProviderBitmap | GlyphProviderReference | GlyphProviderSpace | GlyphProviderTtf | GlyphProviderUnihex


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::font::GlyphProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::font::GlyphProviderType"
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
                    "registry": "minecraft:glyph_provider"
                }
            },
            {
                "kind": "pair",
                "key": "filter",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": {
                                "kind": "reference",
                                "path": "::java::assets::font::FontOption"
                            },
                            "type": {
                                "kind": "boolean"
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

