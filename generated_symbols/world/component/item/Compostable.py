# Generated from symbols.json for ::java::world::component::item::Compostable
from dataclasses import dataclass


@dataclass(kw_only=True)
class Compostable:
    layers: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::Compostable": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "layers",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "number_provider"
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}

