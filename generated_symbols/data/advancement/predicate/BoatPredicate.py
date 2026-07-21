# Generated from symbols.json for ::java::data::advancement::predicate::BoatPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.entity.boat.BoatType import BoatType


@dataclass(kw_only=True)
class BoatPredicate:
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

