# Generated from symbols.json for ::java::world::component::item::Explosion
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.component.item.FireworkShape import FireworkShape


@dataclass(kw_only=True)
class Explosion:
    shape: FireworkShape  # The shape of the explosion.
    colors: list[int] | None = None  # Colors of the initial particles of the explosion, randomly selected from. Calculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.
    fade_colors: list[int] | None = None  # Colors of the fading particles of the explosion
    has_trail: bool | None = None  # Added to a firework star via Diamond.
    has_twinkle: bool | None = None  # Added to a firework star via Glowstone Dust.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::Explosion": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The shape of the explosion.",
                "key": "shape",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::item::FireworkShape"
                }
            },
            {
                "kind": "pair",
                "desc": "Colors of the initial particles of the explosion, randomly selected from.\nCalculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.",
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
                "desc": "Colors of the fading particles of the explosion",
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
                "desc": "Added to a firework star via Diamond.",
                "key": "has_trail",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Added to a firework star via Glowstone Dust.",
                "key": "has_twinkle",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

