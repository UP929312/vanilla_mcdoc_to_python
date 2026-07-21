# Generated from symbols.json for ::java::world::item::enchanted_book::EnchantedBook
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.item.ItemBase import ItemBase

if TYPE_CHECKING:
    from generated_symbols.world.item.Enchantment import Enchantment


@dataclass(kw_only=True)
class EnchantedBook(ItemBase):
    StoredEnchantments: list[Enchantment] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::enchanted_book::EnchantedBook": {
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
                "key": "StoredEnchantments",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::item::Enchantment"
                    }
                },
                "optional": True
            }
        ]
    }
}

