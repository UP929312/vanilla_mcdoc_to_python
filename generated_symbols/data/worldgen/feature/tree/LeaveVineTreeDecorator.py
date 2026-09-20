"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::LeaveVineTreeDecorator
Local link to file: generated_symbols/data/worldgen/feature/tree/LeaveVineTreeDecorator.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field


class LeaveVineTreeDecorator(GeneratedModel):
    probability: Annotated[float, Field(ge=0, le=1)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::LeaveVineTreeDecorator": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19"
                            }
                        }
                    }
                ],
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

