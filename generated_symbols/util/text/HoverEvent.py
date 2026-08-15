"""
Generated from symbols.json for ::java::util::text::HoverEvent
Local link to file: generated_symbols/util/text/HoverEvent.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.world.item.ItemStack import ItemStack
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class HoverEventShowEntity:
    action: Literal['minecraft:show_entity']
    id: Annotated[str, IdSpec(registry='entity_type')]
    uuid: tuple[int, int, int, int] | str
    name: Text | None = None


@dataclass(kw_only=True)
class HoverEventShowItem(ItemStack):
    action: Literal['minecraft:show_item']


@dataclass(kw_only=True)
class HoverEventShowText:
    action: Literal['minecraft:show_text']
    value: Text


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

