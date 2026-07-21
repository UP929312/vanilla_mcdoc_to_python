# Generated from symbols.json for ::java::world::component::item::Enchantments
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.component.item.EnchantmentLevels import EnchantmentLevels


@dataclass(kw_only=True)
class Enchantments:
    levels: EnchantmentLevels
    show_in_tooltip: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::Enchantments": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "levels",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::item::EnchantmentLevels"
                }
            },
            {
                "kind": "pair",
                "key": "show_in_tooltip",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

