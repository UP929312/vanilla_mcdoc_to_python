"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::CocoaTreeDecorator
Local link to file: generated_symbols/data/worldgen/feature/tree/CocoaTreeDecorator.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class CocoaTreeDecorator:
    probability: Annotated[float, 'Range | `0`-`1` | both inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::CocoaTreeDecorator": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "probability",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            }
        ]
    }
}

