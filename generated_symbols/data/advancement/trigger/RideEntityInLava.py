# Generated from symbols.json for ::java::data::advancement::trigger::RideEntityInLava
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.advancement.trigger.TriggerBase import TriggerBase

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.DistancePredicate import DistancePredicate
    from generated_symbols.data.advancement.predicate.LocationPredicate import LocationPredicate


@dataclass(kw_only=True)
class RideEntityInLava(TriggerBase):
    start_position: LocationPredicate | None = None
    distance: DistancePredicate | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::RideEntityInLava": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::trigger::TriggerBase"
                }
            },
            {
                "kind": "pair",
                "key": "start_position",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::LocationPredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "distance",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::DistancePredicate"
                },
                "optional": True
            }
        ]
    }
}

