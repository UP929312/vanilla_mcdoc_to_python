"""
Generated from symbols.json for ::java::data::loot::condition::EntityProperties
Local link to file: vanilla_mcdoc/data/loot/condition/EntityProperties.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.predicate.EntityPredicate import EntityPredicate
    from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget


class EntityProperties(GeneratedModel):
    entity: EntityTarget
    predicate: EntityPredicate


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::condition::EntityProperties": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "entity",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::EntityTarget"
                }
            },
            {
                "kind": "pair",
                "key": "predicate",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::EntityPredicate"
                }
            }
        ]
    }
}
