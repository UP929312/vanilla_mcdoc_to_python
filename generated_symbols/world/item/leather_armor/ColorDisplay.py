# Generated from symbols.json for ::java::world::item::leather_armor::ColorDisplay
from dataclasses import dataclass
from generated_symbols.world.item.Display import Display


@dataclass(kw_only=True)
class ColorDisplay(Display):
    color: int | None = None  # Color of the armor. Calculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::leather_armor::ColorDisplay": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::Display"
                }
            },
            {
                "kind": "pair",
                "desc": "Color of the armor.\nCalculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.",
                "key": "color",
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
                },
                "optional": True
            }
        ]
    }
}

