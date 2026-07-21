# Generated from symbols.json for ::java::world::entity::projectile::throwable::ThrowableItem
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.projectile.throwable.Throwable import Throwable

if TYPE_CHECKING:
    from generated_symbols.world.item.ItemStack import ItemStack


@dataclass(kw_only=True)
class ThrowableItem(Throwable):
    Item: ItemStack | None = None  # Item representation of the projectile.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::projectile::throwable::ThrowableItem": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::projectile::throwable::Throwable"
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
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "desc": "Item representation of the projectile.",
                "key": "Item",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemStack"
                },
                "optional": True
            }
        ]
    }
}

