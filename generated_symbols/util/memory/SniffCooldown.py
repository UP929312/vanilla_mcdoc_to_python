# Generated from symbols.json for ::java::util::memory::SniffCooldown
from dataclasses import dataclass
from typing import Any
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class SniffCooldown(ExpirableValue):
    value: Any  # If present, the warden or sniffer will not sniff.


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

