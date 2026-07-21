# Generated from symbols.json for ::java::data::advancement::trigger::EntityKilledPlayer
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.advancement.trigger.TriggerBase import TriggerBase

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.DamageSourcePredicate import DamageSourcePredicate
    from generated_symbols.data.advancement.trigger.CompositeEntity import CompositeEntity


@dataclass(kw_only=True)
class EntityKilledPlayer(TriggerBase):
    entity: CompositeEntity | None = None
    killing_blow: DamageSourcePredicate | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::EntityKilledPlayer": {
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
                "key": "entity",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::trigger::CompositeEntity"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "killing_blow",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::DamageSourcePredicate"
                },
                "optional": True
            }
        ]
    }
}

