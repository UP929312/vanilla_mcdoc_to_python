"""
Generated from symbols.json for ::java::util::text::SpriteText
Local link to file: vanilla_mcdoc/util/text/SpriteText.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.util.text.ObjectTextConfig import ObjectTextConfig
from vanilla_mcdoc.util.text.TextBase import TextBase


class SpriteText(ObjectTextConfig, TextBase):
    atlas: Annotated[str, IdSpec(registry='atlas')] | None = None  # Defaults to `minecraft:blocks`.
    sprite: Annotated[str, IdSpec(registry='texture')]
    object: Literal['atlas'] | None = 'atlas'
    type: Literal['object'] | None = 'object'
