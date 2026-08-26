"""
Generated from symbols.json for ::java::util::text::HoverEvent
Local link to file: generated_symbols/util/text/HoverEvent.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

from generated_symbols.util.text.ShowEntity import ShowEntity
from generated_symbols.util.text.ShowItem import ShowItem
from generated_symbols.util.text.ShowText import ShowText


@dataclass(kw_only=True)
class HoverEventShowEntity(ShowEntity):
    action: Literal['minecraft:show_entity']


@dataclass(kw_only=True)
class HoverEventShowItem(ShowItem):
    action: Literal['minecraft:show_item']


@dataclass(kw_only=True)
class HoverEventShowText(ShowText):
    action: Literal['minecraft:show_text']


type HoverEvent = HoverEventShowEntity | HoverEventShowItem | HoverEventShowText


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

