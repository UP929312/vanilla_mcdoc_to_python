"""
Generated from symbols.json for ::java::util::memory::BreezeShootCooldown
Local link to file: vanilla_mcdoc/util/memory/BreezeShootCooldown.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class ValueStruct(GeneratedModel):
    pass


class BreezeShootCooldown(ExpirableValue):
    value: ValueStruct  # If present, the breeze will not shoot a wind charge. Set after shooting


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::BreezeShootCooldown": {
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
                "desc": "If present, the breeze will not shoot a wind charge. Set after shooting",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}
