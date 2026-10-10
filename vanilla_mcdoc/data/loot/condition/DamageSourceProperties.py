"""
Generated from symbols.json for ::java::data::loot::condition::DamageSourceProperties
Local link to file: vanilla_mcdoc/data/loot/condition/DamageSourceProperties.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.predicate.DamageSourcePredicate import DamageSourcePredicate


class DamageSourceProperties(GeneratedModel):
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
