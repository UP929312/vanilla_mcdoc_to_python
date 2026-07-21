# Generated from symbols.json for ::java::data::loot::condition::DamageSourceProperties
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.DamageSourcePredicate import DamageSourcePredicate


@dataclass(kw_only=True)
class DamageSourceProperties:
    predicate: DamageSourcePredicate


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::condition::DamageSourceProperties": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "predicate",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::DamageSourcePredicate"
                }
            }
        ]
    }
}

