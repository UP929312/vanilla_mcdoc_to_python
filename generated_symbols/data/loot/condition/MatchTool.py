"""
Generated from symbols.json for ::java::data::loot::condition::MatchTool
Local link to file: generated_symbols/data/loot/condition/MatchTool.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate


class MatchTool(GeneratedModel):
    predicate: ItemPredicate


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::condition::MatchTool": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "predicate",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::ItemPredicate"
                }
            }
        ]
    }
}

