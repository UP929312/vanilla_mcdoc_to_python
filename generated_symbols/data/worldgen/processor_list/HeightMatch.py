# Generated from symbols.json for ::java::data::worldgen::processor_list::HeightMatch
from dataclasses import dataclass


@dataclass(kw_only=True)
class HeightMatch:
    min_inclusive: int
    max_inclusive: int


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::HeightMatch": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "min_inclusive",
                "type": {
                    "kind": "int"
                }
            },
            {
                "kind": "pair",
                "key": "max_inclusive",
                "type": {
                    "kind": "int"
                }
            }
        ]
    }
}

