# Generated from symbols.json for ::java::world::entity::projectile::firework_rocket::FireWorkRocket
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.projectile.ProjectileBase import ProjectileBase

if TYPE_CHECKING:
    from generated_symbols.world.item.ItemStack import ItemStack


@dataclass(kw_only=True)
class FireWorkRocket(ProjectileBase):
    Life: int | None = None  # Ticks it has existed.
    LifeTime: int | None = None  # Ticks it will exist.
    ShotAtAngle: bool | None = None  # Whether it should move at an angle.
    FireworksItem: ItemStack | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::projectile::firework_rocket::FireWorkRocket": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::projectile::ProjectileBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Ticks it has existed.",
                "key": "Life",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Ticks it will exist.",
                "key": "LifeTime",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether it should move at an angle.",
                "key": "ShotAtAngle",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "FireworksItem",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemStack"
                },
                "optional": True
            }
        ]
    }
}

