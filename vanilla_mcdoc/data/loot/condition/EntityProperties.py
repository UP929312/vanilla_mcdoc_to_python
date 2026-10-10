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
