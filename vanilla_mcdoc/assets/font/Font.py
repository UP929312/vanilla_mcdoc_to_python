"""
Generated from symbols.json for ::java::assets::font::Font
Local link to file: vanilla_mcdoc/assets/font/Font.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.font.GlyphProvider import GlyphProvider


class Font(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'font'

    providers: list[GlyphProvider]
