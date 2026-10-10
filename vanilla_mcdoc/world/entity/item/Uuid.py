"""
Generated from symbols.json for ::java::world::entity::item::Uuid
Local link to file: generated_symbols/world/entity/item/Uuid.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel


class Uuid(GeneratedModel):
    L: int | None = None  # Lower bits of the target player's UUID
    M: int | None = None  # Upper bits of the target player's UUID


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::item::Uuid": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Lower bits of the target player's UUID",
                "key": "L",
                "type": {
                    "kind": "long"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Upper bits of the target player's UUID",
                "key": "M",
                "type": {
                    "kind": "long"
                },
                "optional": True
            }
        ]
    }
}
