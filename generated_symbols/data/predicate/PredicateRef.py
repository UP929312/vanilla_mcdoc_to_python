# Generated from symbols.json for ::java::data::predicate::PredicateRef
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.predicate.Predicate import Predicate


type PredicateRef = Predicate | str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::predicate::PredicateRef": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::data::predicate::Predicate"
            },
            {
                "kind": "string",
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
                    },
                    {
                        "name": "id",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "predicate"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

