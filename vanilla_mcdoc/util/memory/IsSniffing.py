"""
Generated from symbols.json for ::java::util::memory::IsSniffing
Local link to file: vanilla_mcdoc/util/memory/IsSniffing.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class ValueStruct(GeneratedModel):
    pass


class IsSniffing(ExpirableValue):
    value: ValueStruct  # Whether the warden or sniffer is currently sniffing.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::IsSniffing": {
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
                "desc": "Whether the warden or sniffer is currently sniffing.",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}
