"""
Generated from symbols.json for ::java::util::text::EntityNbtText
Local link to file: vanilla_mcdoc/util/text/EntityNbtText.py
"""
# ~~~ CODE ~~~
from typing import Literal

from vanilla_mcdoc.util.text.TextNbtBase import TextNbtBase


class EntityNbtText(TextNbtBase):
    entity: str
    nbt: str
    source: Literal['entity'] | None = 'entity'
    type: Literal['nbt'] | None = 'nbt'
