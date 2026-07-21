# Generated from symbols.json for ::java::data::worldgen::feature::GeodeCrackSettings
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class GeodeCrackSettings:
    generate_crack_chance: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None
    base_crack_size: Annotated[float, 'Range | `0`-`5` | both inclusive'] | None = None
    crack_point_offset: Annotated[int, 'Range | `0`-`10` | both inclusive'] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::GeodeCrackSettings": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "generate_crack_chance",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "base_crack_size",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 5
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "crack_point_offset",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 10
                    }
                },
                "optional": True
            }
        ]
    }
}

