"""
Generated from symbols.json for ::java::data::advancement::trigger::KilledByArrowTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/KilledByArrowTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.trigger.AdvancementEntityPredicate import AdvancementEntityPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions
from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


class KilledByArrowTriggerTypeArg(PlayerConditions):
    unique_entity_types: MinMaxBounds[int] | int | None = None  # How many different types of entities were killed.
    fired_from_weapon: ItemPredicate | None = None  # The weapon item that was used to fire the arrow.
    victims: list[AdvancementEntityPredicate] | None = None  # Predicate context: Advancement Entity.  Evaluates to true if every predicate in the list matches some victims.


KilledByArrowTrigger = AllOptional[KilledByArrowTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::KilledByArrowTrigger": {
        "kind": "concrete",
        "child": {
            "kind": "reference",
            "path": "::java::data::advancement::trigger::AllOptional"
        },
        "typeArgs": [
            {
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
                        "desc": "How many different types of entities were killed.",
                        "key": "unique_entity_types",
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
                                        "value": "1.21.2"
                                    }
                                }
                            }
                        ],
                        "desc": "The weapon item that was used to fire the arrow.",
                        "key": "fired_from_weapon",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::advancement::predicate::ItemPredicate"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "Predicate context: Advancement Entity. \\\nEvaluates to True if every predicate in the list matches some victims.",
                        "key": "victims",
                        "type": {
                            "kind": "list",
                            "item": {
                                "kind": "reference",
                                "path": "::java::data::advancement::trigger::AdvancementEntityPredicate"
                            }
                        },
                        "optional": True
                    }
                ]
            }
        ]
    }
}
