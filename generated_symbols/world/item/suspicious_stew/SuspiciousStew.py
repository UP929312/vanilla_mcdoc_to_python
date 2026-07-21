# Generated from symbols.json for ::java::world::item::suspicious_stew::SuspiciousStew
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.item.ItemBase import ItemBase

if TYPE_CHECKING:
    from generated_symbols.world.item.suspicious_stew.Effect import Effect


@dataclass(kw_only=True)
class SuspiciousStew(ItemBase):
    Effects: list[Effect] | None = None  # Effects this stew will give.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::suspicious_stew::SuspiciousStew": {
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
                "desc": "Effects this stew will give.",
                "key": "Effects",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::item::suspicious_stew::Effect"
                    }
                },
                "optional": True
            }
        ]
    }
}

