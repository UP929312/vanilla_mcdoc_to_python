"""
Generated from symbols.json for ::java::util::text::NormalText
Local link to file: vanilla_mcdoc/util/text/NormalText.py
"""
# ~~~ CODE ~~~
from typing import Literal

from vanilla_mcdoc.util.text.TextBase import TextBase


class NormalText(TextBase):
    text: str
    type: Literal['text'] | None = 'text'
