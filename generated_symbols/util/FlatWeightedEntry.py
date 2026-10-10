"""
Generated from symbols.json for ::java::util::FlatWeightedEntry
Local link to file: generated_symbols/util/FlatWeightedEntry.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Generic, TypeVar

from pydantic import Field

from generated_symbols.base import GeneratedModel


T = TypeVar('T')

class FlatWeightedEntry(GeneratedModel, Generic[T]):
    weight: Annotated[int, Field(ge=0)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::FlatWeightedEntry": {
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
                    "kind": "spread",
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

