# Generated from symbols.json for ::java::data::worldgen::processor_list::LinearPos
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class LinearPos:
    min_dist: Annotated[int, 'Range | `0`-`255` | both inclusive'] | None = None
    max_dist: Annotated[int, 'Range | `0`-`255` | both inclusive'] | None = None
    min_chance: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None
    max_chance: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::LinearPos": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "min_dist",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 255
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "max_dist",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 255
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "min_chance",
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
                "key": "max_chance",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                },
                "optional": True
            }
        ]
    }
}

