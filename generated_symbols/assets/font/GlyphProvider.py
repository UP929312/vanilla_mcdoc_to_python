"""
Generated from symbols.json for ::java::assets::font::GlyphProvider
Local link to file: generated_symbols/assets/font/GlyphProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Field

from generated_symbols.assets.font.BitmapProvider import BitmapProvider
from generated_symbols.assets.font.ReferenceProvider import ReferenceProvider
from generated_symbols.assets.font.SpaceProvider import SpaceProvider
from generated_symbols.assets.font.TtfProvider import TtfProvider
from generated_symbols.assets.font.UnihexProvider import UnihexProvider

if TYPE_CHECKING:
    from generated_symbols.assets.font.FontOption import FontOption


class GlyphProviderBitmap(BitmapProvider):
    type: Literal['minecraft:bitmap', 'bitmap'] = 'minecraft:bitmap'
    filter: dict[FontOption, bool] | None = None


class GlyphProviderReference(ReferenceProvider):
    type: Literal['minecraft:reference', 'reference'] = 'minecraft:reference'
    filter: dict[FontOption, bool] | None = None


class GlyphProviderSpace(SpaceProvider):
    type: Literal['minecraft:space', 'space'] = 'minecraft:space'
    filter: dict[FontOption, bool] | None = None


class GlyphProviderTtf(TtfProvider):
    type: Literal['minecraft:ttf', 'ttf'] = 'minecraft:ttf'
    filter: dict[FontOption, bool] | None = None


class GlyphProviderUnihex(UnihexProvider):
    type: Literal['minecraft:unihex', 'unihex'] = 'minecraft:unihex'
    filter: dict[FontOption, bool] | None = None


type GlyphProvider = Annotated[
    GlyphProviderBitmap | GlyphProviderReference | GlyphProviderSpace | GlyphProviderTtf | GlyphProviderUnihex,
    Field(discriminator='type'),
]


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

