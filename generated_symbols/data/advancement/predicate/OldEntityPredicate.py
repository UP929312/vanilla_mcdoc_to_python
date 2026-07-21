# Generated from symbols.json for ::java::data::advancement::predicate::OldEntityPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Any

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.DistancePredicate import DistancePredicate
    from generated_symbols.data.advancement.predicate.EntityEffectsPredicate import EntityEffectsPredicate
    from generated_symbols.data.advancement.predicate.EntityEquipmentPredicate import EntityEquipmentPredicate
    from generated_symbols.data.advancement.predicate.EntityFlagsPredicate import EntityFlagsPredicate
    from generated_symbols.data.advancement.predicate.EntityPredicate import EntityPredicate
    from generated_symbols.data.advancement.predicate.EntitySlotsPredicate import EntitySlotsPredicate
    from generated_symbols.data.advancement.predicate.EntitySubPredicate import EntitySubPredicate
    from generated_symbols.data.advancement.predicate.EntityTypePredicate import EntityTypePredicate
    from generated_symbols.data.advancement.predicate.LocationPredicate import LocationPredicate
    from generated_symbols.data.advancement.predicate.MovementPredicate import MovementPredicate
    from generated_symbols.world.component.DataComponentExactPredicate import DataComponentExactPredicate
    from generated_symbols.world.component.DataComponentPredicate import DataComponentPredicate


@dataclass(kw_only=True)
class OldEntityPredicate:
    type: EntityTypePredicate | None = None
    type_specific: EntitySubPredicate | None = None
    team: str | None = None
    nbt: str | Any | None = None
    location: LocationPredicate | None = None
    distance: DistancePredicate | None = None
    flags: EntityFlagsPredicate | None = None
    equipment: EntityEquipmentPredicate | None = None
    vehicle: EntityPredicate | None = None
    passenger: EntityPredicate | None = None
    stepping_on: LocationPredicate | None = None
    targeted_entity: EntityPredicate | None = None  # Entity that a mob's AI/aggro is targeting.
    effects: EntityEffectsPredicate | None = None
    slots: EntitySlotsPredicate | None = None
    movement: MovementPredicate | None = None
    periodic_tick: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # True every `n` ticks of an entity's lifetime.
    movement_affected_by: LocationPredicate | None = None  # Whether the block at most 0.5 blocks below the entity is present which can affect its movement.
    components: DataComponentExactPredicate | None = None  # Match exact data component values on the entity.
    predicates: DataComponentPredicate | None = None  # Test data component values on the entity.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::OldEntityPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::EntityTypePredicate"
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
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "type_specific",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::EntitySubPredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "team",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "team"
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "nbt",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "nbt",
                                    "value": {
                                        "kind": "dispatcher",
                                        "parallelIndices": [
                                            {
                                                "kind": "dynamic",
                                                "accessor": [
                                                    "type"
                                                ]
                                            }
                                        ],
                                        "registry": "minecraft:entity"
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "dispatcher",
                            "parallelIndices": [
                                {
                                    "kind": "dynamic",
                                    "accessor": [
                                        "type"
                                    ]
                                }
                            ],
                            "registry": "minecraft:entity",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.20.5"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "location",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::LocationPredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "distance",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::DistancePredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "flags",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::EntityFlagsPredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "equipment",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::EntityEquipmentPredicate"
                },
                "optional": True
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
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "player",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::PlayerPredicate"
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
                "key": "vehicle",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::EntityPredicate"
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
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "key": "passenger",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::EntityPredicate"
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
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "key": "stepping_on",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::LocationPredicate"
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
                "desc": "Entity that a mob's AI/aggro is targeting.",
                "key": "targeted_entity",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::EntityPredicate"
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
                    },
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "fishing_hook",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::FishingHookPredicate"
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
                                "value": "1.17"
                            }
                        }
                    },
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "lightning_bolt",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::LightningBoltPredicate"
                },
                "optional": True
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
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "catType",
                "type": {
                    "kind": "string"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "effects",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::EntityEffectsPredicate"
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
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "key": "slots",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::EntitySlotsPredicate"
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
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "key": "movement",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::MovementPredicate"
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
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "desc": "True every `n` ticks of an entity's lifetime.",
                "key": "periodic_tick",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
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
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "desc": "Whether the block at most 0.5 blocks below the entity is present which can affect its movement.",
                "key": "movement_affected_by",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::LocationPredicate"
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
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "Match exact data component values on the entity.",
                "key": "components",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::DataComponentExactPredicate"
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
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "Test data component values on the entity.",
                "key": "predicates",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::DataComponentPredicate"
                },
                "optional": True
            }
        ]
    }
}

