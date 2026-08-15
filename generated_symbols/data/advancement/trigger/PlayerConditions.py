"""
Generated from symbols.json for ::java::data::advancement::trigger::PlayerConditions
Local link to file: generated_symbols/data/advancement/trigger/PlayerConditions.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.advancement.trigger.AdvancementEntityPredicate import AdvancementEntityPredicate


@dataclass(kw_only=True)
class PlayerConditions:
    player: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::PlayerConditions": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "desc": "Predicate context: Advancement Entity.",
                "key": "player",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::trigger::AdvancementEntityPredicate"
                },
                "optional": True
            }
        ]
    }
}

