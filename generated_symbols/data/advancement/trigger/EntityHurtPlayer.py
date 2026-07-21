# Generated from symbols.json for ::java::data::advancement::trigger::EntityHurtPlayer
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.advancement.trigger.TriggerBase import TriggerBase

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.DamagePredicate import DamagePredicate


@dataclass(kw_only=True)
class EntityHurtPlayer(TriggerBase):
    damage: DamagePredicate | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::EntityHurtPlayer": {
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
                "key": "damage",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::DamagePredicate"
                },
                "optional": True
            }
        ]
    }
}

