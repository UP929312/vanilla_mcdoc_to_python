"""
Generated from symbols.json for ::java::data::advancement::trigger::PlayerConditions
Local link to file: vanilla_mcdoc/data/advancement/trigger/PlayerConditions.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.trigger.AdvancementEntityPredicate import AdvancementEntityPredicate


class PlayerConditions(GeneratedModel):
    player: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.
