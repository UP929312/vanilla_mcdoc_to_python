# Generated from symbols.json for ::java::data::advancement::predicate::DamageSourcePredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.DamageTagPredicate import DamageTagPredicate
    from generated_symbols.data.advancement.predicate.EntityPredicate import EntityPredicate


@dataclass(kw_only=True)
class DamageSourcePredicate:
    tags: list[DamageTagPredicate] | None = None  # Damage type tags that the damage type is in.
    source_entity: EntityPredicate | None = None  # Source of the damage (eg: a skeleton shooting an arrow or player igniting tnt).
    direct_entity: EntityPredicate | None = None  # Direct entity responsible for the damage (eg: the arrow or tnt).
    is_direct: bool | None = None  # Damage is direct when its direct and source entities are the same.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::DamageSourcePredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19.4"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "is_explosion",
                            "type": {
                                "kind": "boolean"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "is_fire",
                            "type": {
                                "kind": "boolean"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "is_magic",
                            "type": {
                                "kind": "boolean"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "is_projectile",
                            "type": {
                                "kind": "boolean"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "is_lightning",
                            "type": {
                                "kind": "boolean"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "bypasses_armor",
                            "type": {
                                "kind": "boolean"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "bypasses_invulnerability",
                            "type": {
                                "kind": "boolean"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "bypasses_magic",
                            "type": {
                                "kind": "boolean"
                            },
                            "optional": True
                        }
                    ]
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
                                "value": "1.19.4"
                            }
                        }
                    }
                ],
                "desc": "Damage type tags that the damage type is in.",
                "key": "tags",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::advancement::predicate::DamageTagPredicate"
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Source of the damage (eg: a skeleton shooting an arrow or player igniting tnt).",
                "key": "source_entity",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::EntityPredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Direct entity responsible for the damage (eg: the arrow or tnt).",
                "key": "direct_entity",
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
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "desc": "Damage is direct when its direct and source entities are the same.",
                "key": "is_direct",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

