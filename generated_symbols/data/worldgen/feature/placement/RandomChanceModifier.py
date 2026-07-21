# Generated from symbols.json for ::java::data::worldgen::feature::placement::RandomChanceModifier
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class RandomChanceModifier:
    chance: Annotated[float, 'Range | `0`-`1` | both inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::placement::RandomChanceModifier": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "chance",
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

