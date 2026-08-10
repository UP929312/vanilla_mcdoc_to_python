"""
Generated from symbols.json for ::java::data::worldgen::processor_list::HeightMatch
Local link to file: generated_symbols/data/worldgen/processor_list/HeightMatch.py
"""
# ~~~ CODE ~~~
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

