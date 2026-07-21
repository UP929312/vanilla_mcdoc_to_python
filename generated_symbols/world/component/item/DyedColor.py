# Generated from symbols.json for ::java::world::component::item::DyedColor
from dataclasses import dataclass


@dataclass(kw_only=True)
class DyedColor:
    rgb: int  # Color of the armor. Calculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.
    show_in_tooltip: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::DyedColor": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Color of the armor.\nCalculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.",
                "key": "rgb",
                "type": {
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
                }
            },
            {
                "kind": "pair",
                "key": "show_in_tooltip",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

