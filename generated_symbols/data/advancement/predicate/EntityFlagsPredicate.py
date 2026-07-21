# Generated from symbols.json for ::java::data::advancement::predicate::EntityFlagsPredicate
from dataclasses import dataclass


@dataclass(kw_only=True)
class EntityFlagsPredicate:
    is_on_fire: bool | None = None
    is_sneaking: bool | None = None
    is_sprinting: bool | None = None
    is_swimming: bool | None = None
    is_baby: bool | None = None
    is_on_ground: bool | None = None
    is_flying: bool | None = None
    is_in_water: bool | None = None
    is_fall_flying: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::EntityFlagsPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "is_on_fire",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "is_sneaking",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "is_sprinting",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "is_swimming",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "is_baby",
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
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "key": "is_on_ground",
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
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "key": "is_flying",
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
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "key": "is_in_water",
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
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "key": "is_fall_flying",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

