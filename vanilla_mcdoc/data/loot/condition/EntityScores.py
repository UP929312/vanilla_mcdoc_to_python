"""
Generated from symbols.json for ::java::data::loot::condition::EntityScores
Local link to file: vanilla_mcdoc/data/loot/condition/EntityScores.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget
    from vanilla_mcdoc.data.loot.IntRange import IntRange


class EntityScores(GeneratedModel):
    entity: EntityTarget
    scores: dict[str, IntRange]
