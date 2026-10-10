"""
Generated from symbols.json for ::java::world::component::item::Enchantments
Local link to file: vanilla_mcdoc/world/component/item/Enchantments.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.item.EnchantmentLevels import EnchantmentLevels


class Enchantments(GeneratedModel):
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
