"""
Generated from symbols.json for ::java::world::entity::projectile::LlamaSpit
Local link to file: vanilla_mcdoc/world/entity/projectile/LlamaSpit.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.projectile.ProjectileBase import ProjectileBase


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
