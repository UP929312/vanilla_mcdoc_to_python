# Generated from symbols.json for ::java::data::sulfur_cube_archetype::ExplosionData
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class ExplosionData:
    fuse: Annotated[int, 'Range | Min `1` and above | inclusive']  # The fuse time in ticks when ignited.  When ignited by an explosion, the fuse will be a random value between `explosion_fuse / 8` and `3 * explosion_fuse / 8`.
    power: Annotated[int, 'Range | Min `0` and above | inclusive']  # The explosion power.
    causes_fire: bool  # Whether the explosion causes fire.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::sulfur_cube_archetype::ExplosionData": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The fuse time in ticks when ignited. \\\nWhen ignited by an explosion, the fuse will be a random value between `explosion_fuse / 8` and `3 * explosion_fuse / 8`.",
                "key": "fuse",
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
                "desc": "The explosion power.",
                "key": "power",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "Whether the explosion causes fire.",
                "key": "causes_fire",
                "type": {
                    "kind": "boolean"
                }
            }
        ]
    }
}

