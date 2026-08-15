"""
Generated from symbols.json for ::java::data::advancement::trigger::ItemUesdOnLocationConditions
Local link to file: generated_symbols/data/advancement/trigger/ItemUesdOnLocationConditions.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions

if TYPE_CHECKING:
    from generated_symbols.data.advancement.trigger.AdvancementLocationPredicate import AdvancementLocationPredicate


@dataclass(kw_only=True)
class ItemUesdOnLocationConditions(PlayerConditions):
    location: AdvancementLocationPredicate | None = None  # Predicate context: Advancement Location.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::ItemUesdOnLocationConditions": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::trigger::PlayerConditions"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20"
                            }
                        }
                    }
                ],
                "key": "item",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::ItemPredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "key": "block",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::BlockPredicate"
                },
                "optional": True
            },
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
                "desc": "Predicate context: Advancement Location.",
                "key": "location",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::trigger::AdvancementLocationPredicate"
                },
                "optional": True
            }
        ]
    }
}

