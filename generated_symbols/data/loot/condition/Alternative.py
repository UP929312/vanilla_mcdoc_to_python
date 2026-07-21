# Generated from symbols.json for ::java::data::loot::condition::Alternative
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.loot.condition.LootCondition import LootCondition


@dataclass(kw_only=True)
class Alternative:
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

