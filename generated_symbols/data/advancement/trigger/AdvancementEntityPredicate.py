"""
Generated from symbols.json for ::java::data::advancement::trigger::AdvancementEntityPredicate
Local link to file: generated_symbols/data/advancement/trigger/AdvancementEntityPredicate.py
"""
# ~~~ CODE ~~~
from generated_symbols.data.predicate.PredicateRef import PredicateRef


type AdvancementEntityPredicate = PredicateRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::AdvancementEntityPredicate": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::data::advancement::predicate::EntityPredicate",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "list",
                "item": {
                    "kind": "reference",
                    "path": "::java::data::loot::LootCondition"
                },
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
                    },
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "reference",
                "path": "::java::data::predicate::PredicateRef",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

