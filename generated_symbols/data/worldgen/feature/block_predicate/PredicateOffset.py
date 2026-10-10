"""
Generated from symbols.json for ::java::data::worldgen::feature::block_predicate::PredicateOffset
Local link to file: generated_symbols/data/worldgen/feature/block_predicate/PredicateOffset.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel


class PredicateOffset(GeneratedModel):
    offset: tuple[Annotated[int, Field(ge=-16, le=16)], Annotated[int, Field(ge=-16, le=16)], Annotated[int, Field(ge=-16, le=16)]] | None = None  # The block offset to check.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::block_predicate::PredicateOffset": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The block offset to check.",
                "key": "offset",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "int",
                        "valueRange": {
                            "kind": 0,
                            "min": -16,
                            "max": 16
                        }
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                },
                "optional": True
            }
        ]
    }
}

