# Generated from symbols.json for ::java::data::worldgen::feature::SmallDripstoneConfig
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class SmallDripstoneConfig:
    max_placements: Annotated[int, 'Range | `0`-`100` | both inclusive'] | None = None
    empty_space_search_radius: Annotated[int, 'Range | `0`-`20` | both inclusive'] | None = None
    max_offset_from_origin: Annotated[int, 'Range | `0`-`20` | both inclusive'] | None = None
    chance_of_taller_dripstone: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::SmallDripstoneConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "max_placements",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 100
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "empty_space_search_radius",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 20
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "max_offset_from_origin",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 20
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "chance_of_taller_dripstone",
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

