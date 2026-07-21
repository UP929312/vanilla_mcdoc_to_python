# Generated from symbols.json for ::java::util::memory::IsSniffing
from dataclasses import dataclass
from typing import Any
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class IsSniffing(ExpirableValue):
    value: Any  # Whether the warden or sniffer is currently sniffing.


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

