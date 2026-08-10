"""
Generated from symbols.json for ::java::data::predicate::PredicateRef
Local link to file: generated_symbols/data/predicate/PredicateRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.predicate.Predicate import Predicate


type PredicateRef = Predicate | Annotated[str, IdSpec(registry='predicate')]


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

