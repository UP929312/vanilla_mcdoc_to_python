# Generated from symbols.json for ::java::world::component::item::Unbreakable
from dataclasses import dataclass


@dataclass(kw_only=True)
class Unbreakable:
    pass


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::Unbreakable": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
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
                    }
                ],
                "key": "show_in_tooltip",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

