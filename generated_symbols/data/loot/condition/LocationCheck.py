"""
Generated from symbols.json for ::java::data::loot::condition::LocationCheck
Local link to file: generated_symbols/data/loot/condition/LocationCheck.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.LocationPredicate import LocationPredicate


class LocationCheck(GeneratedModel):
    offsetX: int | None = None
    offsetY: int | None = None
    offsetZ: int | None = None
    predicate: LocationPredicate


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::condition::LocationCheck": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "offsetX",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "offsetY",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "offsetZ",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "predicate",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::LocationPredicate"
                }
            }
        ]
    }
}

