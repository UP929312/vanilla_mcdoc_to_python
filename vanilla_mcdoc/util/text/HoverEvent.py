"""
Generated from symbols.json for ::java::util::text::HoverEvent
Local link to file: vanilla_mcdoc/util/text/HoverEvent.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.util.text.ShowEntity import ShowEntity
from vanilla_mcdoc.util.text.ShowItem import ShowItem
from vanilla_mcdoc.util.text.ShowText import ShowText


class HoverEventShowEntity(ShowEntity):
    action: Literal['minecraft:show_entity', 'show_entity'] = 'minecraft:show_entity'


class HoverEventShowItem(ShowItem):
    action: Literal['minecraft:show_item', 'show_item'] = 'minecraft:show_item'


class HoverEventShowText(ShowText):
    action: Literal['minecraft:show_text', 'show_text'] = 'minecraft:show_text'


type HoverEvent = Annotated[
    HoverEventShowEntity | HoverEventShowItem | HoverEventShowText,
    Field(discriminator='action'),
]
