# Generated from symbols.json for ::java::data::advancement::trigger::TameAnimal
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.advancement.trigger.TriggerBase import TriggerBase

if TYPE_CHECKING:
    from generated_symbols.data.advancement.trigger.CompositeEntity import CompositeEntity


@dataclass(kw_only=True)
class TameAnimal(TriggerBase):
    entity: CompositeEntity | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::TameAnimal": {
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
            }
        ]
    }
}

