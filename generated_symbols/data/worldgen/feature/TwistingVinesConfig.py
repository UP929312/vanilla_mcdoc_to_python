# Generated from symbols.json for ::java::data::worldgen::feature::TwistingVinesConfig
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class TwistingVinesConfig:
    spread_width: Annotated[int, 'Range | Min `1` and above | inclusive']
    spread_height: Annotated[int, 'Range | Min `1` and above | inclusive']
    max_height: Annotated[int, 'Range | Min `1` and above | inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::TwistingVinesConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "spread_width",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            },
            {
                "kind": "pair",
                "key": "spread_height",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            },
            {
                "kind": "pair",
                "key": "max_height",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            }
        ]
    }
}

