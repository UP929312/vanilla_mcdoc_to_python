"""
Generated from symbols.json for ::java::data::advancement::trigger::ItemUesdOnLocationConditions
Local link to file: vanilla_mcdoc/data/advancement/trigger/ItemUesdOnLocationConditions.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.trigger.AdvancementLocationPredicate import AdvancementLocationPredicate


class ItemUesdOnLocationConditions(PlayerConditions):
    location: AdvancementLocationPredicate | None = None  # Predicate context: Advancement Location.
