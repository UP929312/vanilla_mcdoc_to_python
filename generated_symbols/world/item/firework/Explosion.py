# Generated from symbols.json for ::java::world::item::firework::Explosion
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.item.firework.ExplosionType import ExplosionType


@dataclass(kw_only=True)
class Explosion:
    Flicker: bool | None = None  # Whether the explosion should flicker.
    Trail: bool | None = None  # Whether the explosion should have a trail.
    Type: ExplosionType | None = None
    Colors: list[int] | None = None  # Colors of the explosion. Calculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.
    FadeColors: list[int] | None = None  # Colors of the explosion fade. Calculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::firework::Explosion": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Whether the explosion should flicker.",
                "key": "Flicker",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the explosion should have a trail.",
                "key": "Trail",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "Type",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::firework::ExplosionType"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Colors of the explosion.\nCalculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.",
                "key": "Colors",
                "type": {
                    "kind": "int_array",
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
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Colors of the explosion fade.\nCalculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.",
                "key": "FadeColors",
                "type": {
                    "kind": "int_array",
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
                "optional": True
            }
        ]
    }
}

