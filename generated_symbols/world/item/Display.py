# Generated from symbols.json for ::java::world::item::Display
from dataclasses import dataclass


@dataclass(kw_only=True)
class Display:
    Name: str | None = None  # A JSON text component.
    Lore: list[str] | None = None  # A list of JSON text components, each element being a lore line.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::Display": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "A JSON text component.",
                "key": "Name",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "text_component"
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "A list of JSON text components, each element being a lore line.",
                "key": "Lore",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string",
                        "attributes": [
                            {
                                "name": "text_component"
                            }
                        ]
                    }
                },
                "optional": True
            }
        ]
    }
}

