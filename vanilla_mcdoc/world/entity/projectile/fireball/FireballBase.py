"""
Generated from symbols.json for ::java::world::entity::projectile::fireball::FireballBase
Local link to file: vanilla_mcdoc/world/entity/projectile/fireball/FireballBase.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.entity.projectile.fireball.DespawnableProjectileBase import DespawnableProjectileBase

if TYPE_CHECKING:
    from vanilla_mcdoc.world.item.ItemStack import ItemStack


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
