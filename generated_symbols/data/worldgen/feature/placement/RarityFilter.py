# Generated from symbols.json for ::java::data::worldgen::feature::placement::RarityFilter
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class RarityFilter:
    chance: Annotated[int, 'Range | Min `0` and above | inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::placement::RarityFilter": {
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

