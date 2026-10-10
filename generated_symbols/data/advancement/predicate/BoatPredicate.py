"""
Generated from symbols.json for ::java::data::advancement::predicate::BoatPredicate
Local link to file: generated_symbols/data/advancement/predicate/BoatPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.world.entity.boat.BoatType import BoatType


class BoatPredicate(GeneratedModel):
    variant: BoatType


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::BoatPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "variant",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::boat::BoatType"
                }
            }
        ]
    }
}
