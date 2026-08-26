"""
Generated from symbols.json for ::java::data::worldgen::feature::TwistingVinesConfig
Local link to file: generated_symbols/data/worldgen/feature/TwistingVinesConfig.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated, ClassVar


@dataclass(kw_only=True)
class TwistingVinesConfig:
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    spread_width: Annotated[int, 'Range | `1` and above | inclusive']
    spread_height: Annotated[int, 'Range | `1` and above | inclusive']
    max_height: Annotated[int, 'Range | `1` and above | inclusive']


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

