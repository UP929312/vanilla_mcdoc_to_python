# Generated from symbols.json for ::java::world::block::conduit::TargetUuid
from dataclasses import dataclass


@dataclass(kw_only=True)
class TargetUuid:
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

