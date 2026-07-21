# Generated from symbols.json for ::java::data::advancement::trigger::DefaultBlockUse
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.advancement.trigger.TriggerBase import TriggerBase

if TYPE_CHECKING:
    from generated_symbols.data.advancement.trigger.AdvancementPredicateRef import AdvancementPredicateRef


@dataclass(kw_only=True)
class DefaultBlockUse(TriggerBase):
    location: AdvancementPredicateRef | None = None  # The location of the block.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::DefaultBlockUse": {
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
                "desc": "The location of the block.",
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

