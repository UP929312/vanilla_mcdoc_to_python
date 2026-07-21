# Generated from symbols.json for ::java::data::advancement::trigger::Levitation
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.advancement.trigger.TriggerBase import TriggerBase

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.DistancePredicate import DistancePredicate
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


@dataclass(kw_only=True)
class Levitation(TriggerBase):
    distance: DistancePredicate | None = None
    duration: MinMaxBounds[int] | int | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::Levitation": {
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
                "key": "distance",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::DistancePredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "duration",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::util::MinMaxBounds"
                    },
                    "typeArgs": [
                        {
                            "kind": "int"
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

