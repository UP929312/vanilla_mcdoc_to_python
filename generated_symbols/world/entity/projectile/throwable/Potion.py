# Generated from symbols.json for ::java::world::entity::projectile::throwable::Potion
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.projectile.throwable.Throwable import Throwable

if TYPE_CHECKING:
    from generated_symbols.world.item.ItemStack import ItemStack


@dataclass(kw_only=True)
class Potion(Throwable):
    Item: ItemStack | None = None  # Item representation of the potion.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::projectile::throwable::Potion": {
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
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "desc": "Item representation of the potion.",
                "key": "Potion",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemStack"
                },
                "optional": True
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
                "desc": "Item representation of the potion.",
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

