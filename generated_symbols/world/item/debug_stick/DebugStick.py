# Generated from symbols.json for ::java::world::item::debug_stick::DebugStick
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.item.ItemBase import ItemBase

if TYPE_CHECKING:
    from generated_symbols.world.component.item.DebugStickState import DebugStickState


@dataclass(kw_only=True)
class DebugStick(ItemBase):
    DebugProperty: DebugStickState | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::debug_stick::DebugStick": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemBase"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "DebugProperty",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::item::DebugStickState"
                },
                "optional": True
            }
        ]
    }
}

