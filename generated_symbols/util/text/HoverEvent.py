"""
Generated from symbols.json for ::java::util::text::HoverEvent
Local link to file: generated_symbols/util/text/HoverEvent.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from generated_symbols.util.text.ShowEntity import ShowEntity
from generated_symbols.util.text.ShowItem import ShowItem
from generated_symbols.util.text.ShowText import ShowText


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


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::HoverEvent": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "action",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::HoverEventAction"
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
                                "action"
                            ]
                        }
                    ],
                    "registry": "minecraft:hover_event"
                }
            }
        ]
    }
}

