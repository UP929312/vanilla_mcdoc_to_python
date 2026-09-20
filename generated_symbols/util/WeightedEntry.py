"""
Generated from symbols.json for ::java::util::WeightedEntry
Local link to file: generated_symbols/util/WeightedEntry.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Generic, TypeVar

from generated_symbols.base import GeneratedModel
from pydantic import Field


T = TypeVar('T')

class WeightedEntry(GeneratedModel, Generic[T]):
    weight: Annotated[int, Field(ge=0)]
    data: T


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::WeightedEntry": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "key": "weight",
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
                    "key": "data",
                    "type": {
                        "kind": "reference",
                        "path": "::java::util::T"
                    }
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::util::T"
            }
        ]
    }
}

