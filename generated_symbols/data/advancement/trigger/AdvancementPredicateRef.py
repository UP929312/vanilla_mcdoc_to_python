# Generated from symbols.json for ::java::data::advancement::trigger::AdvancementPredicateRef
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.predicate.PredicateRef import PredicateRef


type AdvancementPredicateRef = PredicateRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::AdvancementPredicateRef": {
        "kind": "union",
        "members": [
            {
                "kind": "list",
                "item": {
                    "kind": "reference",
                    "path": "::java::data::loot::LootCondition"
                },
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

