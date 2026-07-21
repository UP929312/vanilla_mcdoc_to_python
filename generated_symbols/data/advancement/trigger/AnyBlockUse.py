# Generated from symbols.json for ::java::data::advancement::trigger::AnyBlockUse
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.advancement.trigger.TriggerBase import TriggerBase

if TYPE_CHECKING:
    from generated_symbols.data.advancement.trigger.AdvancementPredicateRef import AdvancementPredicateRef


@dataclass(kw_only=True)
class AnyBlockUse(TriggerBase):
    location: AdvancementPredicateRef | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::AnyBlockUse": {
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
                "key": "location",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::trigger::AdvancementPredicateRef"
                },
                "optional": True
            }
        ]
    }
}

