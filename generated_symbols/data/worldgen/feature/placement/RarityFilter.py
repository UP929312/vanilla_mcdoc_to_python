"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::RarityFilter
Local link to file: generated_symbols/data/worldgen/feature/placement/RarityFilter.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field


class RarityFilter(GeneratedModel):
    chance: Annotated[int, Field(ge=0)]


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

