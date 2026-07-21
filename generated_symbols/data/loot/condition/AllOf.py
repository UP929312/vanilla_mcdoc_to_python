# Generated from symbols.json for ::java::data::loot::condition::AllOf
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.predicate.PredicateListRef import PredicateListRef


@dataclass(kw_only=True)
class AllOf:
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

