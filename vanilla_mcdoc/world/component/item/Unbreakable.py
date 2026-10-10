"""
Generated from symbols.json for ::java::world::component::item::Unbreakable
Local link to file: vanilla_mcdoc/world/component/item/Unbreakable.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class Unbreakable(GeneratedModel):
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
