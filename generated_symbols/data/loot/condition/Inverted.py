# Generated from symbols.json for ::java::data::loot::condition::Inverted
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.predicate.PredicateRef import PredicateRef


@dataclass(kw_only=True)
class Inverted:
    term: PredicateRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::condition::Inverted": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "term",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::predicate::PredicateRef"
                }
            }
        ]
    }
}

