# Generated from symbols.json for ::java::world::entity::projectile::ProjectileBase
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.EntityBase import EntityBase

if TYPE_CHECKING:
    from generated_symbols.world.component.item.AdventureModePredicate import AdventureModePredicate


@dataclass(kw_only=True)
class ProjectileBase(EntityBase):
    HasBeenShot: bool | None = None  # Whether it has been shot. This is set to true when it exists for at least one tick, and is used by the game to ensure it only triggers the projectile_shoot game event once.
    Owner: tuple[int, int, int, int] | None = None
    LeftOwner: bool | None = None  # Whether it has left its owner.
    can_break: AdventureModePredicate | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::projectile::ProjectileBase": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::EntityBase"
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
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "desc": "Whether it has been shot. This is set to True when it exists for\nat least one tick, and is used by the game to ensure it only triggers the projectile_shoot\ngame event once.",
                "key": "HasBeenShot",
                "type": {
                    "kind": "boolean"
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
                "key": "Owner",
                "type": {
                    "kind": "int_array",
                    "lengthRange": {
                        "kind": 0,
                        "min": 4,
                        "max": 4
                    },
                    "attributes": [
                        {
                            "name": "uuid"
                        }
                    ]
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
                "desc": "Whether it has left its owner.",
                "key": "LeftOwner",
                "type": {
                    "kind": "boolean"
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
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "can_break",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::item::AdventureModePredicate"
                },
                "optional": True
            }
        ]
    }
}

