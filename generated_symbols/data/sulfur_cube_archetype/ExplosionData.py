"""
Generated from symbols.json for ::java::data::sulfur_cube_archetype::ExplosionData
Local link to file: generated_symbols/data/sulfur_cube_archetype/ExplosionData.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field


class ExplosionData(GeneratedModel):
    fuse: Annotated[int, Field(ge=1)]  # The fuse time in ticks when ignited.  When ignited by an explosion, the fuse will be a random value between `explosion_fuse / 8` and `3 * explosion_fuse / 8`.
    power: Annotated[int, Field(ge=0)]  # The explosion power.
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

