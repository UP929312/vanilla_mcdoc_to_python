"""
Generated from symbols.json for ::java::world::block::conduit::TargetUuid
Local link to file: generated_symbols/world/block/conduit/TargetUuid.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel


class TargetUuid(GeneratedModel):
    M: int | None = None  # Upper bits of the target's UUID
    L: int | None = None  # Lower bits of the target's UUID


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::conduit::TargetUuid": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Upper bits of the target's UUID",
                "key": "M",
                "type": {
                    "kind": "long"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Lower bits of the target's UUID",
                "key": "L",
                "type": {
                    "kind": "long"
                },
                "optional": True
            }
        ]
    }
}

