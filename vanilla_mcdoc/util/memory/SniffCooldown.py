"""
Generated from symbols.json for ::java::util::memory::SniffCooldown
Local link to file: vanilla_mcdoc/util/memory/SniffCooldown.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class ValueStruct(GeneratedModel):
    pass


class SniffCooldown(ExpirableValue):
    value: ValueStruct  # If present, the warden or sniffer will not sniff.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::SniffCooldown": {
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
                "desc": "If present, the warden or sniffer will not sniff.",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}
