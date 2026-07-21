# Generated from symbols.json for ::java::data::worldgen::feature::decorator::ChanceConfig
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class ChanceConfig:
    chance: Annotated[int, 'Range | Min `0` and above | inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::decorator::ChanceConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "chance",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                }
            }
        ]
    }
}

