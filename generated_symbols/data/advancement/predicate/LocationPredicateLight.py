"""
Generated from symbols.json for ::java::data::advancement::predicate::LocationPredicateLight
Local link to file: generated_symbols/data/advancement/predicate/LocationPredicateLight.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


class LocationPredicateLight(GeneratedModel):
    light: MinMaxBounds[Annotated[int, Field(ge=0, le=15)]] | Annotated[int, Field(ge=0, le=15)] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::LocationPredicateLight": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "light",
                "type": {
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
                                "min": 0,
                                "max": 15
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

