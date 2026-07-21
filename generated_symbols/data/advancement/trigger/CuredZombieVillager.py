# Generated from symbols.json for ::java::data::advancement::trigger::CuredZombieVillager
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.advancement.trigger.TriggerBase import TriggerBase

if TYPE_CHECKING:
    from generated_symbols.data.advancement.trigger.CompositeEntity import CompositeEntity


@dataclass(kw_only=True)
class CuredZombieVillager(TriggerBase):
    villager: CompositeEntity | None = None
    zombie: CompositeEntity | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::CuredZombieVillager": {
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
                "key": "villager",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::trigger::CompositeEntity"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "zombie",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::trigger::CompositeEntity"
                },
                "optional": True
            }
        ]
    }
}

