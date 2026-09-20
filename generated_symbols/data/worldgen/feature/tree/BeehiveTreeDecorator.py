"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::BeehiveTreeDecorator
Local link to file: generated_symbols/data/worldgen/feature/tree/BeehiveTreeDecorator.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field


class BeehiveTreeDecorator(GeneratedModel):
    probability: Annotated[float, Field(ge=0, le=1)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::BeehiveTreeDecorator": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "probability",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            }
        ]
    }
}

