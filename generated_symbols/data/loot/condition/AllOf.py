"""
Generated from symbols.json for ::java::data::loot::condition::AllOf
Local link to file: generated_symbols/data/loot/condition/AllOf.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.predicate.PredicateListRef import PredicateListRef


class AllOf(GeneratedModel):
    terms: PredicateListRef  # Passes when all of these conditions pass.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::condition::AllOf": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Passes when all of these conditions pass.",
                "key": "terms",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::predicate::PredicateListRef"
                }
            }
        ]
    }
}

