"""
Generated from symbols.json for ::java::data::advancement::trigger::BeeNestDestroyedTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/BeeNestDestroyedTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions
from vanilla_mcdoc.util.registry_ref.BlockListRef import BlockListRef


class BeeNestDestroyedTriggerTypeArg(PlayerConditions):
    blocks: BlockListRef | None = None
    state: dict[str, str] | None = None
    num_bees_inside: int | None = None  # Number of bees that were inside the bee nest/beehive before it was broken.
    item: ItemPredicate | None = None  # Item used to break the block.


BeeNestDestroyedTrigger = AllOptional[BeeNestDestroyedTriggerTypeArg]
