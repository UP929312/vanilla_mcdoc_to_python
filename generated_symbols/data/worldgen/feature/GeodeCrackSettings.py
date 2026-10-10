"""
Generated from symbols.json for ::java::data::worldgen::feature::GeodeCrackSettings
Local link to file: generated_symbols/data/worldgen/feature/GeodeCrackSettings.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel


class GeodeCrackSettings(GeneratedModel):
    generate_crack_chance: Annotated[float, Field(ge=0, le=1)] | None = None
    base_crack_size: Annotated[float, Field(ge=0, le=5)] | None = None
    crack_point_offset: Annotated[int, Field(ge=0, le=10)] | None = None


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

