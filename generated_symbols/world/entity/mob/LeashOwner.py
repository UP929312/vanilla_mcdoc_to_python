"""
Generated from symbols.json for ::java::world::entity::mob::LeashOwner
Local link to file: generated_symbols/world/entity/mob/LeashOwner.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel


class LeashOwner(GeneratedModel):
    UUID: tuple[int, int, int, int] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::LeashOwner": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "UUID",
                "type": {
                    "kind": "int_array",
                    "lengthRange": {
                        "kind": 0,
                        "min": 4,
                        "max": 4
                    }
                },
                "optional": True
            }
        ]
    }
}

