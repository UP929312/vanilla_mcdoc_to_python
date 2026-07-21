# Generated from symbols.json for ::java::world::entity::mob::LeashOwner
from dataclasses import dataclass


@dataclass(kw_only=True)
class LeashOwner:
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

