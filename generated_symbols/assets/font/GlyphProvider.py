"""
Generated from symbols.json for ::java::assets::font::GlyphProvider
Local link to file: generated_symbols/assets/font/GlyphProvider.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.assets.font.FontOption import FontOption
    from generated_symbols.assets.font.UnihexOverrideRange import UnihexOverrideRange


@dataclass(kw_only=True)
class GlyphProviderBitmap:
    type: Literal['minecraft:bitmap']
    filter: dict[FontOption, bool] | None = None
    file: str
    height: int | None = None
    ascent: int
    chars: Annotated[list[Annotated[str, 'Length = 1 (inclusive) and above']], 'Length = 1 (inclusive) and above']


@dataclass(kw_only=True)
class GlyphProviderReference:
    type: Literal['minecraft:reference']
    filter: dict[FontOption, bool] | None = None
    id: Annotated[str, IdSpec(registry='font')]


@dataclass(kw_only=True)
class GlyphProviderSpace:
    type: Literal['minecraft:space']
    filter: dict[FontOption, bool] | None = None
    advances: dict[Annotated[str, 'Length = Exactly 1'], float]


@dataclass(kw_only=True)
class GlyphProviderTtf:
    type: Literal['minecraft:ttf']
    filter: dict[FontOption, bool] | None = None
    file: str
    size: float | None = None
    oversample: float | None = None
    shift: tuple[float, float] | None = None
    skip: str | list[str] | None = None


@dataclass(kw_only=True)
class GlyphProviderUnihex:
    type: Literal['minecraft:unihex']
    filter: dict[FontOption, bool] | None = None
    hex_file: str  # ZIP archive containing one or more *.hex files (files in archive with different extensions are ignored).
    size_overrides: list[UnihexOverrideRange] | None = None  # List of ranges to override the size of.


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

