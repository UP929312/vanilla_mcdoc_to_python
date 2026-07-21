# Generated from symbols.json for ::java::world::entity::projectile::LlamaSpit
from dataclasses import dataclass
from generated_symbols.world.entity.projectile.ProjectileBase import ProjectileBase


@dataclass(kw_only=True)
class LlamaSpit(ProjectileBase):
    pass


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::projectile::LlamaSpit": {
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
                "key": "Owner",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::projectile::OwnerUuid",
                    "attributes": [
                        {
                            "name": "uuid"
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

