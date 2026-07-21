# Generated from symbols.json for ::java::util::memory::RecentProjectile
from dataclasses import dataclass
from typing import Any
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class RecentProjectile(ExpirableValue):
    value: Any  # Whether the warden has recently noticed a projectile vibration.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::RecentProjectile": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::memory::ExpirableValue"
                }
            },
            {
                "kind": "pair",
                "desc": "Whether the warden has recently noticed a projectile vibration.",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}

