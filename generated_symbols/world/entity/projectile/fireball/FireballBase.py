# Generated from symbols.json for ::java::world::entity::projectile::fireball::FireballBase
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.projectile.fireball.DespawnableProjectileBase import DespawnableProjectileBase

if TYPE_CHECKING:
    from generated_symbols.world.item.ItemStack import ItemStack


@dataclass(kw_only=True)
class FireballBase(DespawnableProjectileBase):
    Item: ItemStack | None = None  # Item it should render as.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::projectile::fireball::FireballBase": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::projectile::fireball::DespawnableProjectileBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Item it should render as.",
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

