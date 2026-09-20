"""
Generated from symbols.json for ::java::util::memory::RecentProjectile
Local link to file: generated_symbols/util/memory/RecentProjectile.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


class ValueStruct(GeneratedModel):
    pass


class RecentProjectile(ExpirableValue):
    value: ValueStruct  # Whether the warden has recently noticed a projectile vibration.


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

