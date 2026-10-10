"""
Generated from symbols.json for ::java::util::text::SelectorText
Local link to file: vanilla_mcdoc/util/text/SelectorText.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Literal

from vanilla_mcdoc.util.text.TextBase import TextBase

if TYPE_CHECKING:
    from vanilla_mcdoc.util.text.Text import Text


class SelectorText(TextBase):
    selector: str
    separator: Text | None = None
    type: Literal['selector'] | None = 'selector'
