"""
Generated from symbols.json for ::java::data::loot::condition::Inverted
Local link to file: generated_symbols/data/loot/condition/Inverted.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.predicate.PredicateRef import PredicateRef


class Inverted(GeneratedModel):
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
