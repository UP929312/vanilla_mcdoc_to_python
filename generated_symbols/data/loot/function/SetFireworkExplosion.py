# Generated from symbols.json for ::java::data::loot::function::SetFireworkExplosion
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from generated_symbols.world.component.item.FireworkShape import FireworkShape


@dataclass(kw_only=True)
class SetFireworkExplosion(Conditions):
    shape: FireworkShape | None = None  # If omitted, the original shape is kept (or `small_ball` is used if there was no component).
    colors: list[int] | None = None  # If omitted, the original colors are kept (or `[]` is used if there was no component). Calculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.
    fade_colors: list[int] | None = None  # If omitted, the original fade colors are kept (or `[]` is used if there was no component). Calculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.
    trail: bool | None = None  # If omitted, the original `has_trail` value is kept (or `false` is used if there was no component).
    twinkle: bool | None = None  # If omitted, the original `has_twinkle` value is kept (or `false` is used if there was no component).


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::SetFireworkExplosion": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "If omitted, the original shape is kept (or `small_ball` is used if there was no component).",
                "key": "shape",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::item::FireworkShape"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "If omitted, the original colors are kept (or `[]` is used if there was no component).\nCalculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.",
                "key": "colors",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "int_array",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.5"
                                        }
                                    }
                                },
                                {
                                    "name": "color",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "composite_rgb"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "list",
                            "item": {
                                "kind": "int",
                                "attributes": [
                                    {
                                        "name": "color",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "composite_rgb"
                                            }
                                        }
                                    }
                                ]
                            },
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
                            ]
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "If omitted, the original fade colors are kept (or `[]` is used if there was no component).\nCalculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.",
                "key": "fade_colors",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "int_array",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.5"
                                        }
                                    }
                                },
                                {
                                    "name": "color",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "composite_rgb"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "list",
                            "item": {
                                "kind": "int",
                                "attributes": [
                                    {
                                        "name": "color",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "composite_rgb"
                                            }
                                        }
                                    }
                                ]
                            },
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
                            ]
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "If omitted, the original `has_trail` value is kept (or `False` is used if there was no component).",
                "key": "trail",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "If omitted, the original `has_twinkle` value is kept (or `False` is used if there was no component).",
                "key": "twinkle",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::Conditions"
                }
            }
        ]
    }
}

