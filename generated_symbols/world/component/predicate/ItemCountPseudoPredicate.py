"""
Generated from symbols.json for ::java::world::component::predicate::ItemCountPseudoPredicate
Local link to file: generated_symbols/world/component/predicate/ItemCountPseudoPredicate.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from generated_symbols.data.util.MinMaxBounds import MinMaxBounds
from pydantic import Field


ItemCountPseudoPredicate = MinMaxBounds[Annotated[int, Field(ge=1, le=99)]] | Annotated[int, Field(ge=1, le=99)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::predicate::ItemCountPseudoPredicate": {
        "kind": "concrete",
        "child": {
            "kind": "reference",
            "path": "::java::data::util::MinMaxBounds"
        },
        "typeArgs": [
            {
                "kind": "int",
                "valueRange": {
                    "kind": 0,
                    "min": 1,
                    "max": 99
                }
            }
        ]
    }
}

