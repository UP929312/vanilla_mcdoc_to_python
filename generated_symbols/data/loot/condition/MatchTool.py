# Generated from symbols.json for ::java::data::loot::condition::MatchTool
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate


@dataclass(kw_only=True)
class MatchTool:
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

