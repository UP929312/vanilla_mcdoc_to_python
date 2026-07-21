# Generated from symbols.json for ::java::util::memory::ExpirableValue
from dataclasses import dataclass


@dataclass(kw_only=True)
class ExpirableValue:
    ttl: int | None = None  # If present, ticks before this memory is automatically removed.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::ExpirableValue": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "desc": "If present, ticks before this memory is automatically removed.",
                "key": "ttl",
                "type": {
                    "kind": "long"
                },
                "optional": True
            }
        ]
    }
}

