"""
Generated from symbols.json for ::java::util::text::TextNbtBase
Local link to file: vanilla_mcdoc/util/text/TextNbtBase.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.util.text.TextBase import TextBase

if TYPE_CHECKING:
    from vanilla_mcdoc.util.text.Text import Text


class TextNbtBase(TextBase):
    interpret: bool | None = None
    plain: bool | None = None  # Whether to remove colors from pretty-printed NBT structure when `interpret` is `false`. Defaults to `false`.  Cannot be `true` when `interpret` is `true`.
    separator: Text | None = None
