"""
Generated from symbols.json for ::java::data::worldgen::processor_list::BlockAge
Local link to file: generated_symbols/data/worldgen/processor_list/BlockAge.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass


@dataclass(kw_only=True)
class BlockAge:
    mossiness: float


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::BlockAge": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "mossiness",
                "type": {
                    "kind": "float"
                }
            }
        ]
    }
}

