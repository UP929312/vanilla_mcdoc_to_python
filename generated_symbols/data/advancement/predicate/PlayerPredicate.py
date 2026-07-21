# Generated from symbols.json for ::java::data::advancement::predicate::PlayerPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.EntityPredicate import EntityPredicate
    from generated_symbols.data.advancement.predicate.GameMode import GameMode
    from generated_symbols.data.advancement.predicate.StatisticPredicate import StatisticPredicate
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


@dataclass(kw_only=True)
class PlayerPredicate:
    advancements: dict[str, bool | dict[str, bool]] | None = None
    gamemode: list[GameMode] | None = None
    level: MinMaxBounds[int] | int | None = None  # Experience/XP level.
    recipes: dict[str, bool] | None = None
    stats: list[StatisticPredicate] | None = None
    looking_at: EntityPredicate | None = None
    input: Any | None = None  # Checks the movement keys of the player.
    food: Any | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::PlayerPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "advancements",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "advancement"
                                            }
                                        }
                                    }
                                ]
                            },
                            "type": {
                                "kind": "union",
                                "members": [
                                    {
                                        "kind": "boolean"
                                    },
                                    {
                                        "kind": "struct",
                                        "fields": [
                                            {
                                                "kind": "pair",
                                                "key": {
                                                    "kind": "string"
                                                },
                                                "type": {
                                                    "kind": "boolean"
                                                }
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "gamemode",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::data::advancement::predicate::GameMode",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "list",
                            "item": {
                                "kind": "reference",
                                "path": "::java::data::advancement::predicate::GameMode"
                            },
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
                            ]
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Experience/XP level.",
                "key": "level",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::util::MinMaxBounds"
                    },
                    "typeArgs": [
                        {
                            "kind": "int"
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "recipes",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "recipe"
                                            }
                                        }
                                    }
                                ]
                            },
                            "type": {
                                "kind": "boolean"
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "stats",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::advancement::predicate::StatisticPredicate"
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "looking_at",
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
                                "value": "1.21.2"
                            }
                        }
                    }
                ],
                "desc": "Checks the movement keys of the player.",
                "key": "input",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "forward",
                            "type": {
                                "kind": "boolean"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "backward",
                            "type": {
                                "kind": "boolean"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "left",
                            "type": {
                                "kind": "boolean"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "right",
                            "type": {
                                "kind": "boolean"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "jump",
                            "type": {
                                "kind": "boolean"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "sneak",
                            "type": {
                                "kind": "boolean"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "sprint",
                            "type": {
                                "kind": "boolean"
                            },
                            "optional": True
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
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "key": "food",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "level",
                            "type": {
                                "kind": "concrete",
                                "child": {
                                    "kind": "reference",
                                    "path": "::java::data::util::MinMaxBounds"
                                },
                                "typeArgs": [
                                    {
                                        "kind": "int"
                                    }
                                ]
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "saturation",
                            "type": {
                                "kind": "concrete",
                                "child": {
                                    "kind": "reference",
                                    "path": "::java::data::util::MinMaxBounds"
                                },
                                "typeArgs": [
                                    {
                                        "kind": "double"
                                    }
                                ]
                            },
                            "optional": True
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

