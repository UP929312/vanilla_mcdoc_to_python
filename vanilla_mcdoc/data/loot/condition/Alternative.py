"""
Generated from symbols.json for ::java::data::loot::condition::Alternative
Local link to file: generated_symbols/data/loot/condition/Alternative.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.loot.condition.LootCondition import LootCondition


class Alternative(GeneratedModel):
    terms: list[LootCondition]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::condition::Alternative": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "terms",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::loot::condition::LootCondition"
                    }
                }
            }
        ]
    }
}
