"""
Generated from symbols.json for ::java::util::memory::RecentProjectile
Local link to file: vanilla_mcdoc/util/memory/RecentProjectile.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


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
