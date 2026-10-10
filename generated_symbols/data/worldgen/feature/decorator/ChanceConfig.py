"""
Generated from symbols.json for ::java::data::worldgen::feature::decorator::ChanceConfig
Local link to file: generated_symbols/data/worldgen/feature/decorator/ChanceConfig.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel


class ChanceConfig(GeneratedModel):
    chance: Annotated[int, Field(ge=0)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::decorator::ChanceConfig": {
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
