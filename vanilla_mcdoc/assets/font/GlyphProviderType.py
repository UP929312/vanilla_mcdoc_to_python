"""
Generated from symbols.json for ::java::assets::font::GlyphProviderType
Local link to file: vanilla_mcdoc/assets/font/GlyphProviderType.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class GlyphProviderType(StrEnum):
    BITMAP = "bitmap"
    TRUETYPE = "ttf"
    SPACE = "space"
    UNIHEX = "unihex"
    REFERENCE = "reference"
