"""Vanilla's data/advancement/story/ files"""
from vanilla_mcdoc.data.advancement.Advancement import Advancement
from vanilla_mcdoc.data.advancement.AdvancementCriterion import AdvancementCriterionChangedDimension, AdvancementCriterionCuredZombieVillager, AdvancementCriterionEnchantedItem, AdvancementCriterionEntityHurtPlayer, AdvancementCriterionInventoryChanged, AdvancementCriterionLocation
from vanilla_mcdoc.data.advancement.AdvancementDisplay import AdvancementDisplay
from vanilla_mcdoc.data.advancement.AdvancementFrame import AdvancementFrame
from vanilla_mcdoc.data.advancement.RootAdvancementDisplay import RootAdvancementDisplay
from vanilla_mcdoc.data.advancement.predicate.DamagePredicate import DamagePredicate
from vanilla_mcdoc.data.advancement.predicate.DamageSourcePredicate import DamageSourcePredicate
from vanilla_mcdoc.data.advancement.predicate.DamageTagPredicate import DamageTagPredicate
from vanilla_mcdoc.data.advancement.predicate.EntitySubPredicateMap import EntitySubPredicateMap
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.predicate.LocationPredicate import LocationPredicate
from vanilla_mcdoc.data.advancement.trigger.ChangeDimensionTrigger import ChangeDimensionTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.EntityHurtPlayerTrigger import EntityHurtPlayerTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.InventoryChangeTrigger import InventoryChangeTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions
from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget
from vanilla_mcdoc.data.loot.condition.LootCondition import LootConditionEntityProperties
from vanilla_mcdoc.util.text.TextObject import TextObjectStruct2
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

CURE_ZOMBIE_VILLAGER = Advancement(
    parent='minecraft:story/enter_the_nether',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:golden_apple'),
        title=TextObjectStruct2(translate='advancements.story.cure_zombie_villager.title'),
        description=TextObjectStruct2(translate='advancements.story.cure_zombie_villager.description'),
        frame=AdvancementFrame.GOAL,
    ),
    criteria={'cured_zombie': AdvancementCriterionCuredZombieVillager(trigger='minecraft:cured_zombie_villager')},
    requirements=[['cured_zombie']],
    sends_telemetry_event=True,
)

DEFLECT_ARROW = Advancement(
    parent='minecraft:story/obtain_armor',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:shield'),
        title=TextObjectStruct2(translate='advancements.story.deflect_arrow.title'),
        description=TextObjectStruct2(translate='advancements.story.deflect_arrow.description'),
    ),
    criteria={
        'deflected_projectile': AdvancementCriterionEntityHurtPlayer(
            conditions=EntityHurtPlayerTriggerTypeArg(
                damage=DamagePredicate(
                    blocked=True,
                    type=DamageSourcePredicate(tags=[DamageTagPredicate(id='#minecraft:is_projectile', expected=True)]),
                ),
            ),
            trigger='minecraft:entity_hurt_player',
        ),
    },
    requirements=[['deflected_projectile']],
    sends_telemetry_event=True,
)

ENCHANT_ITEM = Advancement(
    parent='minecraft:story/mine_diamond',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:enchanted_book'),
        title=TextObjectStruct2(translate='advancements.story.enchant_item.title'),
        description=TextObjectStruct2(translate='advancements.story.enchant_item.description'),
    ),
    criteria={'enchanted_item': AdvancementCriterionEnchantedItem(trigger='minecraft:enchanted_item')},
    requirements=[['enchanted_item']],
    sends_telemetry_event=True,
)

ENTER_THE_END = Advancement(
    parent='minecraft:story/follow_ender_eye',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:end_stone'),
        title=TextObjectStruct2(translate='advancements.story.enter_the_end.title'),
        description=TextObjectStruct2(translate='advancements.story.enter_the_end.description'),
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

ENTER_THE_NETHER = Advancement(
    parent='minecraft:story/form_obsidian',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:flint_and_steel'),
        title=TextObjectStruct2(translate='advancements.story.enter_the_nether.title'),
        description=TextObjectStruct2(translate='advancements.story.enter_the_nether.description'),
    ),
    criteria={
        'entered_nether': AdvancementCriterionChangedDimension(
            conditions=ChangeDimensionTriggerTypeArg(to='minecraft:the_nether'),
            trigger='minecraft:changed_dimension',
        ),
    },
    requirements=[['entered_nether']],
    sends_telemetry_event=True,
)

FOLLOW_ENDER_EYE = Advancement(
    parent='minecraft:story/enter_the_nether',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:ender_eye'),
        title=TextObjectStruct2(translate='advancements.story.follow_ender_eye.title'),
        description=TextObjectStruct2(translate='advancements.story.follow_ender_eye.description'),
    ),
    criteria={
        'in_stronghold': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(structures='minecraft:stronghold')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
    },
    requirements=[['in_stronghold']],
    sends_telemetry_event=True,
)

FORM_OBSIDIAN = Advancement(
    parent='minecraft:story/lava_bucket',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:obsidian'),
        title=TextObjectStruct2(translate='advancements.story.form_obsidian.title'),
        description=TextObjectStruct2(translate='advancements.story.form_obsidian.description'),
    ),
    criteria={
        'obsidian': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:obsidian')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['obsidian']],
    sends_telemetry_event=True,
)

IRON_TOOLS = Advancement(
    parent='minecraft:story/smelt_iron',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:iron_pickaxe'),
        title=TextObjectStruct2(translate='advancements.story.iron_tools.title'),
        description=TextObjectStruct2(translate='advancements.story.iron_tools.description'),
    ),
    criteria={
        'iron_pickaxe': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_pickaxe')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['iron_pickaxe']],
    sends_telemetry_event=True,
)

LAVA_BUCKET = Advancement(
    parent='minecraft:story/smelt_iron',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:lava_bucket'),
        title=TextObjectStruct2(translate='advancements.story.lava_bucket.title'),
        description=TextObjectStruct2(translate='advancements.story.lava_bucket.description'),
    ),
    criteria={
        'lava_bucket': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lava_bucket')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['lava_bucket']],
    sends_telemetry_event=True,
)

MINE_DIAMOND = Advancement(
    parent='minecraft:story/iron_tools',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:diamond'),
        title=TextObjectStruct2(translate='advancements.story.mine_diamond.title'),
        description=TextObjectStruct2(translate='advancements.story.mine_diamond.description'),
    ),
    criteria={
        'diamond': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:diamond')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['diamond']],
    sends_telemetry_event=True,
)

MINE_STONE = Advancement(
    parent='minecraft:story/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:wooden_pickaxe'),
        title=TextObjectStruct2(translate='advancements.story.mine_stone.title'),
        description=TextObjectStruct2(translate='advancements.story.mine_stone.description'),
    ),
    criteria={
        'get_stone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:stone_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['get_stone']],
    sends_telemetry_event=True,
)

OBTAIN_ARMOR = Advancement(
    parent='minecraft:story/smelt_iron',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:iron_chestplate'),
        title=TextObjectStruct2(translate='advancements.story.obtain_armor.title'),
        description=TextObjectStruct2(translate='advancements.story.obtain_armor.description'),
    ),
    criteria={
        'iron_boots': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_boots')]),
            trigger='minecraft:inventory_changed',
        ),
        'iron_chestplate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_chestplate')]),
            trigger='minecraft:inventory_changed',
        ),
        'iron_helmet': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_helmet')]),
            trigger='minecraft:inventory_changed',
        ),
        'iron_leggings': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_leggings')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['iron_helmet', 'iron_chestplate', 'iron_leggings', 'iron_boots']],
    sends_telemetry_event=True,
)

ROOT = Advancement(
    display=RootAdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:grass_block'),
        title=TextObjectStruct2(translate='advancements.story.root.title'),
        description=TextObjectStruct2(translate='advancements.story.root.description'),
        show_toast=False,
        announce_to_chat=False,
        background='minecraft:gui/advancements/backgrounds/stone',
    ),
    criteria={
        'crafting_table': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:crafting_table')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['crafting_table']],
    sends_telemetry_event=True,
)

SHINY_GEAR = Advancement(
    parent='minecraft:story/mine_diamond',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:diamond_chestplate'),
        title=TextObjectStruct2(translate='advancements.story.shiny_gear.title'),
        description=TextObjectStruct2(translate='advancements.story.shiny_gear.description'),
    ),
    criteria={
        'diamond_boots': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:diamond_boots')]),
            trigger='minecraft:inventory_changed',
        ),
        'diamond_chestplate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:diamond_chestplate')]),
            trigger='minecraft:inventory_changed',
        ),
        'diamond_helmet': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:diamond_helmet')]),
            trigger='minecraft:inventory_changed',
        ),
        'diamond_leggings': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:diamond_leggings')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['diamond_helmet', 'diamond_chestplate', 'diamond_leggings', 'diamond_boots']],
    sends_telemetry_event=True,
)

SMELT_IRON = Advancement(
    parent='minecraft:story/upgrade_tools',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:iron_ingot'),
        title=TextObjectStruct2(translate='advancements.story.smelt_iron.title'),
        description=TextObjectStruct2(translate='advancements.story.smelt_iron.description'),
    ),
    criteria={
        'iron': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['iron']],
    sends_telemetry_event=True,
)

UPGRADE_TOOLS = Advancement(
    parent='minecraft:story/mine_stone',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:stone_pickaxe'),
        title=TextObjectStruct2(translate='advancements.story.upgrade_tools.title'),
        description=TextObjectStruct2(translate='advancements.story.upgrade_tools.description'),
    ),
    criteria={
        'stone_pickaxe': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stone_pickaxe')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['stone_pickaxe']],
    sends_telemetry_event=True,
)
