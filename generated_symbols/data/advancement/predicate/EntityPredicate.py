# Generated from symbols.json for ::java::data::advancement::predicate::EntityPredicate
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.EntitySubPredicateMap import EntitySubPredicateMap


type EntityPredicate = EntitySubPredicateMap


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::EntityPredicate": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::data::advancement::predicate::OldEntityPredicate",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.2"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "reference",
                "path": "::java::data::advancement::predicate::EntitySubPredicateMap",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.2"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

