# Generated from symbols.json for ::java::world::entity::projectile::arrow::Trident
from dataclasses import dataclass
from generated_symbols.world.entity.projectile.arrow.ArrowBase import ArrowBase


@dataclass(kw_only=True)
class Trident(ArrowBase):
    DealtDamage: bool | None = None  # Whether it has already damaged an entity.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::projectile::arrow::Trident": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::projectile::arrow::ArrowBase"
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
                                "value": "1.20.3"
                            }
                        }
                    }
                ],
                "key": "Trident",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemStack"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether it has already damaged an entity.",
                "key": "DealtDamage",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

