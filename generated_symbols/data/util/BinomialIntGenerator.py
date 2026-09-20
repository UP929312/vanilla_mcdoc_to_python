"""
Generated from symbols.json for ::java::data::util::BinomialIntGenerator
Local link to file: generated_symbols/data/util/BinomialIntGenerator.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field


class BinomialIntGenerator(GeneratedModel):
    n: Annotated[int, Field(ge=0)]
    p: Annotated[float, Field(ge=0, le=1)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::util::BinomialIntGenerator": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "n",
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
                "key": "p",
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

