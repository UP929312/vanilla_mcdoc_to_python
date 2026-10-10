"""
Generated from symbols.json for ::java::util::text::BlockNbtText
Local link to file: vanilla_mcdoc/util/text/BlockNbtText.py
"""
# ~~~ CODE ~~~
from typing import Literal

from vanilla_mcdoc.util.text.TextNbtBase import TextNbtBase


class BlockNbtText(TextNbtBase):
    block: str
    nbt: str
    source: Literal['block'] | None = 'block'
    type: Literal['nbt'] | None = 'nbt'
