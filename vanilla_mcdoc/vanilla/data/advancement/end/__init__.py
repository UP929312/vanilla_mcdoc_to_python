"""Vanilla's data/advancement/end/ files"""
from vanilla_mcdoc.data.advancement.Advancement import Advancement
from vanilla_mcdoc.data.advancement.AdvancementCriterion import AdvancementCriterionChangedDimension, AdvancementCriterionEnterBlock, AdvancementCriterionInventoryChanged, AdvancementCriterionLevitation, AdvancementCriterionLocation, AdvancementCriterionPlayerKilledEntity, AdvancementCriterionSummonedEntity
from vanilla_mcdoc.data.advancement.AdvancementDisplay import AdvancementDisplay
from vanilla_mcdoc.data.advancement.AdvancementFrame import AdvancementFrame
from vanilla_mcdoc.data.advancement.AdvancementRewards import AdvancementRewards
from vanilla_mcdoc.data.advancement.RootAdvancementDisplay import RootAdvancementDisplay
from vanilla_mcdoc.data.advancement.predicate.DistancePredicate import DistancePredicate
from vanilla_mcdoc.data.advancement.predicate.EntitySubPredicateMap import EntitySubPredicateMap
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.predicate.LocationPredicate import LocationPredicate
from vanilla_mcdoc.data.advancement.trigger.ChangeDimensionTrigger import ChangeDimensionTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.EnterBlockTrigger import EnterBlockTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.InventoryChangeTrigger import InventoryChangeTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.KilledTrigger import KilledTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.LevitationTrigger import LevitationTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions
from vanilla_mcdoc.data.advancement.trigger.SummonedEntityTrigger import SummonedEntityTriggerTypeArg
from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget
from vanilla_mcdoc.data.loot.condition.LootCondition import LootConditionEntityProperties
from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds
from vanilla_mcdoc.util.text.TextObject import TextObjectStruct2
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

DRAGON_BREATH = Advancement(
    parent='minecraft:end/kill_dragon',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:dragon_breath'),
        title=TextObjectStruct2(translate='advancements.end.dragon_breath.title'),
        description=TextObjectStruct2(translate='advancements.end.dragon_breath.description'),
        frame=AdvancementFrame.GOAL,
    ),
    criteria={
        'dragon_breath': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dragon_breath')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['dragon_breath']],
    sends_telemetry_event=True,
)

DRAGON_EGG = Advancement(
    parent='minecraft:end/kill_dragon',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:dragon_egg'),
        title=TextObjectStruct2(translate='advancements.end.dragon_egg.title'),
        description=TextObjectStruct2(translate='advancements.end.dragon_egg.description'),
        frame=AdvancementFrame.GOAL,
    ),
    criteria={
        'dragon_egg': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dragon_egg')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['dragon_egg']],
    sends_telemetry_event=True,
)

ELYTRA = Advancement(
    parent='minecraft:end/find_end_city',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:elytra'),
        title=TextObjectStruct2(translate='advancements.end.elytra.title'),
        description=TextObjectStruct2(translate='advancements.end.elytra.description'),
        frame=AdvancementFrame.GOAL,
    ),
    criteria={
        'elytra': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:elytra')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['elytra']],
    sends_telemetry_event=True,
)

ENTER_END_GATEWAY = Advancement(
    parent='minecraft:end/kill_dragon',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:ender_pearl'),
        title=TextObjectStruct2(translate='advancements.end.enter_end_gateway.title'),
        description=TextObjectStruct2(translate='advancements.end.enter_end_gateway.description'),
    ),
    criteria={
        'entered_end_gateway': AdvancementCriterionEnterBlock(
            conditions=EnterBlockTriggerTypeArg(blocks='minecraft:end_gateway'),
            trigger='minecraft:enter_block',
        ),
    },
    requirements=[['entered_end_gateway']],
    sends_telemetry_event=True,
)

FIND_END_CITY = Advancement(
    parent='minecraft:end/enter_end_gateway',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:purpur_block'),
        title=TextObjectStruct2(translate='advancements.end.find_end_city.title'),
        description=TextObjectStruct2(translate='advancements.end.find_end_city.description'),
    ),
    criteria={
        'in_city': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(structures='minecraft:end_city')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
    },
    requirements=[['in_city']],
    sends_telemetry_event=True,
)

KILL_DRAGON = Advancement(
    parent='minecraft:end/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:dragon_head'),
        title=TextObjectStruct2(translate='advancements.end.kill_dragon.title'),
        description=TextObjectStruct2(translate='advancements.end.kill_dragon.description'),
    ),
    criteria={
        'killed_dragon': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:ender_dragon'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
    },
    requirements=[['killed_dragon']],
    sends_telemetry_event=True,
)

LEVITATE = Advancement(
    parent='minecraft:end/find_end_city',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:shulker_shell'),
        title=TextObjectStruct2(translate='advancements.end.levitate.title'),
        description=TextObjectStruct2(translate='advancements.end.levitate.description'),
        frame=AdvancementFrame.CHALLENGE,
    ),
    criteria={
        'levitated': AdvancementCriterionLevitation(
            conditions=LevitationTriggerTypeArg(distance=DistancePredicate(y=MinMaxBounds(min=50.0))),
            trigger='minecraft:levitation',
        ),
    },
    requirements=[['levitated']],
    rewards=AdvancementRewards(experience=50),
    sends_telemetry_event=True,
)

RESPAWN_DRAGON = Advancement(
    parent='minecraft:end/kill_dragon',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:end_crystal'),
        title=TextObjectStruct2(translate='advancements.end.respawn_dragon.title'),
        description=TextObjectStruct2(translate='advancements.end.respawn_dragon.description'),
        frame=AdvancementFrame.GOAL,
    ),
    criteria={
        'summoned_dragon': AdvancementCriterionSummonedEntity(
            conditions=SummonedEntityTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:ender_dragon'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:summoned_entity',
        ),
    },
    requirements=[['summoned_dragon']],
    sends_telemetry_event=True,
)

ROOT = Advancement(
    display=RootAdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:end_stone'),
        title=TextObjectStruct2(translate='advancements.end.root.title'),
        description=TextObjectStruct2(translate='advancements.end.root.description'),
        show_toast=False,
        announce_to_chat=False,
        background='minecraft:gui/advancements/backgrounds/end',
    ),
    criteria={
        'entered_end': AdvancementCriterionChangedDimension(
            conditions=ChangeDimensionTriggerTypeArg(to='minecraft:the_end'),
            trigger='minecraft:changed_dimension',
        ),
    },
    requirements=[['entered_end']],
    sends_telemetry_event=True,
)
