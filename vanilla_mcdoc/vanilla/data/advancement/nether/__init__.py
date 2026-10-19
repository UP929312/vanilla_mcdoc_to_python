"""Vanilla's data/advancement/nether/ files"""
from vanilla_mcdoc.data.advancement.Advancement import Advancement
from vanilla_mcdoc.data.advancement.AdvancementCriterion import AdvancementCriterionBrewedPotion, AdvancementCriterionChangedDimension, AdvancementCriterionConstructBeacon, AdvancementCriterionEffectsChanged, AdvancementCriterionInventoryChanged, AdvancementCriterionItemDurabilityChanged, AdvancementCriterionItemUsedOnBlock, AdvancementCriterionLocation, AdvancementCriterionNetherTravel, AdvancementCriterionPlayerGeneratesContainerLoot, AdvancementCriterionPlayerInteractedWithEntity, AdvancementCriterionPlayerKilledEntity, AdvancementCriterionRideEntityInLava, AdvancementCriterionSummonedEntity, AdvancementCriterionThrownItemPickedUpByEntity
from vanilla_mcdoc.data.advancement.AdvancementDisplay import AdvancementDisplay
from vanilla_mcdoc.data.advancement.AdvancementFrame import AdvancementFrame
from vanilla_mcdoc.data.advancement.AdvancementRewards import AdvancementRewards
from vanilla_mcdoc.data.advancement.RootAdvancementDisplay import RootAdvancementDisplay
from vanilla_mcdoc.data.advancement.predicate.BlockPredicate import BlockPredicate
from vanilla_mcdoc.data.advancement.predicate.DamageSourcePredicate import DamageSourcePredicate
from vanilla_mcdoc.data.advancement.predicate.DamageTagPredicate import DamageTagPredicate
from vanilla_mcdoc.data.advancement.predicate.DistancePredicate import DistancePredicate
from vanilla_mcdoc.data.advancement.predicate.EntityFlagsPredicate import EntityFlagsPredicate
from vanilla_mcdoc.data.advancement.predicate.EntitySubPredicateMap import EntitySubPredicateMap
from vanilla_mcdoc.data.advancement.predicate.EquipmentPredicateSlot import EquipmentPredicateSlot
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.predicate.LocationPredicate import LocationPredicate
from vanilla_mcdoc.data.advancement.predicate.MobEffectPredicate import MobEffectPredicate
from vanilla_mcdoc.data.advancement.trigger.ChangeDimensionTrigger import ChangeDimensionTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.ConstructBeaconTrigger import ConstructBeaconTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.DistanceTrigger import DistanceTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.EffectsChangedTrigger import EffectsChangedTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.InventoryChangeTrigger import InventoryChangeTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.ItemDurabilityTrigger import ItemDurabilityTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.ItemUesdOnLocationConditions import ItemUesdOnLocationConditions
from vanilla_mcdoc.data.advancement.trigger.KilledTrigger import KilledTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.LootTableTrigger import LootTableTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.NetherTravelTrigger import NetherTravelTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.PickedUpItemTrigger import PickedUpItemTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions
from vanilla_mcdoc.data.advancement.trigger.PlayerInteractTrigger import PlayerInteractTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.SummonedEntityTrigger import SummonedEntityTriggerTypeArg
from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget
from vanilla_mcdoc.data.loot.condition.LootCondition import LootConditionAllOf, LootConditionAnyOf, LootConditionEntityProperties, LootConditionInverted, LootConditionLocationCheck, LootConditionMatchTool
from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds
from vanilla_mcdoc.util.text.TextObject import TextObjectStruct2
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

ALL_EFFECTS = Advancement(
    parent='minecraft:nether/all_potions',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:bucket'),
        title=TextObjectStruct2(translate='advancements.nether.all_effects.title'),
        description=TextObjectStruct2(translate='advancements.nether.all_effects.description'),
        frame=AdvancementFrame.CHALLENGE,
        hidden=True,
    ),
    criteria={
        'all_effects': AdvancementCriterionEffectsChanged(
            conditions=EffectsChangedTriggerTypeArg(
                effects={
                    'minecraft:absorption': MobEffectPredicate(),
                    'minecraft:bad_omen': MobEffectPredicate(),
                    'minecraft:blindness': MobEffectPredicate(),
                    'minecraft:breath_of_the_nautilus': MobEffectPredicate(),
                    'minecraft:conduit_power': MobEffectPredicate(),
                    'minecraft:darkness': MobEffectPredicate(),
                    'minecraft:dolphins_grace': MobEffectPredicate(),
                    'minecraft:fire_resistance': MobEffectPredicate(),
                    'minecraft:glowing': MobEffectPredicate(),
                    'minecraft:haste': MobEffectPredicate(),
                    'minecraft:hero_of_the_village': MobEffectPredicate(),
                    'minecraft:hunger': MobEffectPredicate(),
                    'minecraft:infested': MobEffectPredicate(),
                    'minecraft:invisibility': MobEffectPredicate(),
                    'minecraft:jump_boost': MobEffectPredicate(),
                    'minecraft:levitation': MobEffectPredicate(),
                    'minecraft:mining_fatigue': MobEffectPredicate(),
                    'minecraft:nausea': MobEffectPredicate(),
                    'minecraft:night_vision': MobEffectPredicate(),
                    'minecraft:oozing': MobEffectPredicate(),
                    'minecraft:poison': MobEffectPredicate(),
                    'minecraft:raid_omen': MobEffectPredicate(),
                    'minecraft:regeneration': MobEffectPredicate(),
                    'minecraft:resistance': MobEffectPredicate(),
                    'minecraft:slow_falling': MobEffectPredicate(),
                    'minecraft:slowness': MobEffectPredicate(),
                    'minecraft:speed': MobEffectPredicate(),
                    'minecraft:strength': MobEffectPredicate(),
                    'minecraft:trial_omen': MobEffectPredicate(),
                    'minecraft:water_breathing': MobEffectPredicate(),
                    'minecraft:weakness': MobEffectPredicate(),
                    'minecraft:weaving': MobEffectPredicate(),
                    'minecraft:wind_charged': MobEffectPredicate(),
                    'minecraft:wither': MobEffectPredicate(),
                },
            ),
            trigger='minecraft:effects_changed',
        ),
    },
    requirements=[['all_effects']],
    rewards=AdvancementRewards(experience=1000),
    sends_telemetry_event=True,
)

ALL_POTIONS = Advancement(
    parent='minecraft:nether/brew_potion',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:milk_bucket'),
        title=TextObjectStruct2(translate='advancements.nether.all_potions.title'),
        description=TextObjectStruct2(translate='advancements.nether.all_potions.description'),
        frame=AdvancementFrame.CHALLENGE,
    ),
    criteria={
        'all_effects': AdvancementCriterionEffectsChanged(
            conditions=EffectsChangedTriggerTypeArg(
                effects={
                    'minecraft:fire_resistance': MobEffectPredicate(),
                    'minecraft:infested': MobEffectPredicate(),
                    'minecraft:invisibility': MobEffectPredicate(),
                    'minecraft:jump_boost': MobEffectPredicate(),
                    'minecraft:night_vision': MobEffectPredicate(),
                    'minecraft:oozing': MobEffectPredicate(),
                    'minecraft:poison': MobEffectPredicate(),
                    'minecraft:regeneration': MobEffectPredicate(),
                    'minecraft:resistance': MobEffectPredicate(),
                    'minecraft:slow_falling': MobEffectPredicate(),
                    'minecraft:slowness': MobEffectPredicate(),
                    'minecraft:speed': MobEffectPredicate(),
                    'minecraft:strength': MobEffectPredicate(),
                    'minecraft:water_breathing': MobEffectPredicate(),
                    'minecraft:weakness': MobEffectPredicate(),
                    'minecraft:weaving': MobEffectPredicate(),
                    'minecraft:wind_charged': MobEffectPredicate(),
                },
            ),
            trigger='minecraft:effects_changed',
        ),
    },
    requirements=[['all_effects']],
    rewards=AdvancementRewards(experience=100),
    sends_telemetry_event=True,
)

BREW_POTION = Advancement(
    parent='minecraft:nether/obtain_blaze_rod',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:potion'),
        title=TextObjectStruct2(translate='advancements.nether.brew_potion.title'),
        description=TextObjectStruct2(translate='advancements.nether.brew_potion.description'),
    ),
    criteria={'potion': AdvancementCriterionBrewedPotion(trigger='minecraft:brewed_potion')},
    requirements=[['potion']],
    sends_telemetry_event=True,
)

CHARGE_RESPAWN_ANCHOR = Advancement(
    parent='minecraft:nether/obtain_crying_obsidian',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:respawn_anchor'),
        title=TextObjectStruct2(translate='advancements.nether.charge_respawn_anchor.title'),
        description=TextObjectStruct2(translate='advancements.nether.charge_respawn_anchor.description'),
    ),
    criteria={
        'charge_respawn_anchor': AdvancementCriterionItemUsedOnBlock(
            conditions=ItemUesdOnLocationConditions(
                location=LootConditionAllOf(
                    terms=[
                        LootConditionLocationCheck(
                            predicate=LocationPredicate(
                                block=BlockPredicate(blocks='minecraft:respawn_anchor', state={'charges': '4'}),
                            ),
                            type='minecraft:location_check',
                        ),
                        LootConditionMatchTool(
                            predicate=ItemPredicate(items='minecraft:glowstone'),
                            type='minecraft:match_tool',
                        ),
                    ],
                    type='minecraft:all_of',
                ),
            ),
            trigger='minecraft:item_used_on_block',
        ),
    },
    requirements=[['charge_respawn_anchor']],
    sends_telemetry_event=True,
)

CREATE_BEACON = Advancement(
    parent='minecraft:nether/summon_wither',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:beacon'),
        title=TextObjectStruct2(translate='advancements.nether.create_beacon.title'),
        description=TextObjectStruct2(translate='advancements.nether.create_beacon.description'),
    ),
    criteria={
        'beacon': AdvancementCriterionConstructBeacon(
            conditions=ConstructBeaconTriggerTypeArg(level=MinMaxBounds(min=1)),
            trigger='minecraft:construct_beacon',
        ),
    },
    requirements=[['beacon']],
    sends_telemetry_event=True,
)

CREATE_FULL_BEACON = Advancement(
    parent='minecraft:nether/create_beacon',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:beacon'),
        title=TextObjectStruct2(translate='advancements.nether.create_full_beacon.title'),
        description=TextObjectStruct2(translate='advancements.nether.create_full_beacon.description'),
        frame=AdvancementFrame.GOAL,
    ),
    criteria={
        'beacon': AdvancementCriterionConstructBeacon(
            conditions=ConstructBeaconTriggerTypeArg(level=4),
            trigger='minecraft:construct_beacon',
        ),
    },
    requirements=[['beacon']],
    sends_telemetry_event=True,
)

DISTRACT_PIGLIN = Advancement(
    parent='minecraft:nether/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:gold_ingot'),
        title=TextObjectStruct2(translate='advancements.nether.distract_piglin.title'),
        description=TextObjectStruct2(translate='advancements.nether.distract_piglin.description'),
    ),
    criteria={
        'distract_piglin': AdvancementCriterionThrownItemPickedUpByEntity(
            conditions=PickedUpItemTriggerTypeArg(
                player=LootConditionInverted(
                    term=LootConditionAnyOf(
                        terms=[
                            LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(
                                    equipment={EquipmentPredicateSlot.HEAD: ItemPredicate(items='#minecraft:piglin_safe_armor')},
                                ),
                                type='minecraft:entity_properties',
                            ),
                            LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(
                                    equipment={EquipmentPredicateSlot.CHEST: ItemPredicate(items='#minecraft:piglin_safe_armor')},
                                ),
                                type='minecraft:entity_properties',
                            ),
                            LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(
                                    equipment={EquipmentPredicateSlot.LEGS: ItemPredicate(items='#minecraft:piglin_safe_armor')},
                                ),
                                type='minecraft:entity_properties',
                            ),
                            LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(
                                    equipment={EquipmentPredicateSlot.FEET: ItemPredicate(items='#minecraft:piglin_safe_armor')},
                                ),
                                type='minecraft:entity_properties',
                            ),
                        ],
                        type='minecraft:any_of',
                    ),
                    type='minecraft:inverted',
                ),
                item=ItemPredicate(items='#minecraft:piglin_loved'),
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:piglin', flags=EntityFlagsPredicate(is_baby=False)),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:thrown_item_picked_up_by_entity',
        ),
        'distract_piglin_directly': AdvancementCriterionPlayerInteractedWithEntity(
            conditions=PlayerInteractTriggerTypeArg(
                player=LootConditionInverted(
                    term=LootConditionAnyOf(
                        terms=[
                            LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(
                                    equipment={EquipmentPredicateSlot.HEAD: ItemPredicate(items='#minecraft:piglin_safe_armor')},
                                ),
                                type='minecraft:entity_properties',
                            ),
                            LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(
                                    equipment={EquipmentPredicateSlot.CHEST: ItemPredicate(items='#minecraft:piglin_safe_armor')},
                                ),
                                type='minecraft:entity_properties',
                            ),
                            LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(
                                    equipment={EquipmentPredicateSlot.LEGS: ItemPredicate(items='#minecraft:piglin_safe_armor')},
                                ),
                                type='minecraft:entity_properties',
                            ),
                            LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(
                                    equipment={EquipmentPredicateSlot.FEET: ItemPredicate(items='#minecraft:piglin_safe_armor')},
                                ),
                                type='minecraft:entity_properties',
                            ),
                        ],
                        type='minecraft:any_of',
                    ),
                    type='minecraft:inverted',
                ),
                item=ItemPredicate(items='minecraft:gold_ingot'),
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:piglin', flags=EntityFlagsPredicate(is_baby=False)),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_interacted_with_entity',
        ),
    },
    requirements=[['distract_piglin', 'distract_piglin_directly']],
    sends_telemetry_event=True,
)

EXPLORE_NETHER = Advancement(
    parent='minecraft:nether/ride_strider',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:netherite_boots'),
        title=TextObjectStruct2(translate='advancements.nether.explore_nether.title'),
        description=TextObjectStruct2(translate='advancements.nether.explore_nether.description'),
        frame=AdvancementFrame.CHALLENGE,
    ),
    criteria={
        'minecraft:basalt_deltas': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:basalt_deltas')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:crimson_forest': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:crimson_forest')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:nether_wastes': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:nether_wastes')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:soul_sand_valley': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:soul_sand_valley')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:warped_forest': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:warped_forest')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
    },
    requirements=[
        ['minecraft:nether_wastes'],
        ['minecraft:soul_sand_valley'],
        ['minecraft:crimson_forest'],
        ['minecraft:warped_forest'],
        ['minecraft:basalt_deltas'],
    ],
    rewards=AdvancementRewards(experience=500),
    sends_telemetry_event=True,
)

FAST_TRAVEL = Advancement(
    parent='minecraft:nether/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:map'),
        title=TextObjectStruct2(translate='advancements.nether.fast_travel.title'),
        description=TextObjectStruct2(translate='advancements.nether.fast_travel.description'),
        frame=AdvancementFrame.CHALLENGE,
    ),
    criteria={
        'travelled': AdvancementCriterionNetherTravel(
            conditions=NetherTravelTriggerTypeArg(distance=DistancePredicate(horizontal=MinMaxBounds(min=7000.0))),
            trigger='minecraft:nether_travel',
        ),
    },
    requirements=[['travelled']],
    rewards=AdvancementRewards(experience=100),
    sends_telemetry_event=True,
)

FIND_BASTION = Advancement(
    parent='minecraft:nether/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:polished_blackstone_bricks'),
        title=TextObjectStruct2(translate='advancements.nether.find_bastion.title'),
        description=TextObjectStruct2(translate='advancements.nether.find_bastion.description'),
    ),
    criteria={
        'bastion': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(structures='minecraft:bastion_remnant')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
    },
    requirements=[['bastion']],
    sends_telemetry_event=True,
)

FIND_FORTRESS = Advancement(
    parent='minecraft:nether/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:nether_bricks'),
        title=TextObjectStruct2(translate='advancements.nether.find_fortress.title'),
        description=TextObjectStruct2(translate='advancements.nether.find_fortress.description'),
    ),
    criteria={
        'fortress': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(structures='minecraft:fortress')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
    },
    requirements=[['fortress']],
    sends_telemetry_event=True,
)

GET_WITHER_SKULL = Advancement(
    parent='minecraft:nether/find_fortress',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:wither_skeleton_skull'),
        title=TextObjectStruct2(translate='advancements.nether.get_wither_skull.title'),
        description=TextObjectStruct2(translate='advancements.nether.get_wither_skull.description'),
    ),
    criteria={
        'wither_skull': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:wither_skeleton_skull')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['wither_skull']],
    sends_telemetry_event=True,
)

LOOT_BASTION = Advancement(
    parent='minecraft:nether/find_bastion',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:chest'),
        title=TextObjectStruct2(translate='advancements.nether.loot_bastion.title'),
        description=TextObjectStruct2(translate='advancements.nether.loot_bastion.description'),
    ),
    criteria={
        'loot_bastion_bridge': AdvancementCriterionPlayerGeneratesContainerLoot(
            conditions=LootTableTriggerTypeArg(loot_tables='minecraft:chests/bastion_bridge'),
            trigger='minecraft:player_generates_container_loot',
        ),
        'loot_bastion_hoglin_stable': AdvancementCriterionPlayerGeneratesContainerLoot(
            conditions=LootTableTriggerTypeArg(loot_tables='minecraft:chests/bastion_hoglin_stable'),
            trigger='minecraft:player_generates_container_loot',
        ),
        'loot_bastion_other': AdvancementCriterionPlayerGeneratesContainerLoot(
            conditions=LootTableTriggerTypeArg(loot_tables='minecraft:chests/bastion_other'),
            trigger='minecraft:player_generates_container_loot',
        ),
        'loot_bastion_treasure': AdvancementCriterionPlayerGeneratesContainerLoot(
            conditions=LootTableTriggerTypeArg(loot_tables='minecraft:chests/bastion_treasure'),
            trigger='minecraft:player_generates_container_loot',
        ),
    },
    requirements=[['loot_bastion_other', 'loot_bastion_treasure', 'loot_bastion_hoglin_stable', 'loot_bastion_bridge']],
    sends_telemetry_event=True,
)

NETHERITE_ARMOR = Advancement(
    parent='minecraft:nether/obtain_ancient_debris',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:netherite_chestplate'),
        title=TextObjectStruct2(translate='advancements.nether.netherite_armor.title'),
        description=TextObjectStruct2(translate='advancements.nether.netherite_armor.description'),
        frame=AdvancementFrame.CHALLENGE,
    ),
    criteria={
        'netherite_armor': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(
                items=[
                    ItemPredicate(items='minecraft:netherite_helmet'),
                    ItemPredicate(items='minecraft:netherite_chestplate'),
                    ItemPredicate(items='minecraft:netherite_leggings'),
                    ItemPredicate(items='minecraft:netherite_boots'),
                ],
            ),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['netherite_armor']],
    rewards=AdvancementRewards(experience=100),
    sends_telemetry_event=True,
)

OBTAIN_ANCIENT_DEBRIS = Advancement(
    parent='minecraft:nether/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:ancient_debris'),
        title=TextObjectStruct2(translate='advancements.nether.obtain_ancient_debris.title'),
        description=TextObjectStruct2(translate='advancements.nether.obtain_ancient_debris.description'),
    ),
    criteria={
        'ancient_debris': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:ancient_debris')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['ancient_debris']],
    sends_telemetry_event=True,
)

OBTAIN_BLAZE_ROD = Advancement(
    parent='minecraft:nether/find_fortress',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:blaze_rod'),
        title=TextObjectStruct2(translate='advancements.nether.obtain_blaze_rod.title'),
        description=TextObjectStruct2(translate='advancements.nether.obtain_blaze_rod.description'),
    ),
    criteria={
        'blaze_rod': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blaze_rod')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['blaze_rod']],
    sends_telemetry_event=True,
)

OBTAIN_CRYING_OBSIDIAN = Advancement(
    parent='minecraft:nether/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:crying_obsidian'),
        title=TextObjectStruct2(translate='advancements.nether.obtain_crying_obsidian.title'),
        description=TextObjectStruct2(translate='advancements.nether.obtain_crying_obsidian.description'),
    ),
    criteria={
        'crying_obsidian': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:crying_obsidian')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['crying_obsidian']],
    sends_telemetry_event=True,
)

RETURN_TO_SENDER = Advancement(
    parent='minecraft:nether/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:fire_charge'),
        title=TextObjectStruct2(translate='advancements.nether.return_to_sender.title'),
        description=TextObjectStruct2(translate='advancements.nether.return_to_sender.description'),
        frame=AdvancementFrame.CHALLENGE,
    ),
    criteria={
        'killed_ghast': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:ghast'),
                    type='minecraft:entity_properties',
                ),
                killing_blow=DamageSourcePredicate(
                    tags=[DamageTagPredicate(id='#minecraft:is_projectile', expected=True)],
                    direct_entity=EntitySubPredicateMap(entity_type='minecraft:fireball'),
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
    },
    requirements=[['killed_ghast']],
    rewards=AdvancementRewards(experience=50),
    sends_telemetry_event=True,
)

RIDE_STRIDER = Advancement(
    parent='minecraft:nether/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:warped_fungus_on_a_stick'),
        title=TextObjectStruct2(translate='advancements.nether.ride_strider.title'),
        description=TextObjectStruct2(translate='advancements.nether.ride_strider.description'),
    ),
    criteria={
        'used_warped_fungus_on_a_stick': AdvancementCriterionItemDurabilityChanged(
            conditions=ItemDurabilityTriggerTypeArg(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(vehicle=EntitySubPredicateMap(entity_type='minecraft:strider')),
                    type='minecraft:entity_properties',
                ),
                item=ItemPredicate(items='minecraft:warped_fungus_on_a_stick'),
            ),
            trigger='minecraft:item_durability_changed',
        ),
    },
    requirements=[['used_warped_fungus_on_a_stick']],
    sends_telemetry_event=True,
)

RIDE_STRIDER_IN_OVERWORLD_LAVA = Advancement(
    parent='minecraft:nether/ride_strider',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:warped_fungus_on_a_stick'),
        title=TextObjectStruct2(translate='advancements.nether.ride_strider_in_overworld_lava.title'),
        description=TextObjectStruct2(translate='advancements.nether.ride_strider_in_overworld_lava.description'),
    ),
    criteria={
        'ride_entity_distance': AdvancementCriterionRideEntityInLava(
            conditions=DistanceTriggerTypeArg(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(
                        location=LocationPredicate(dimension='minecraft:overworld'),
                        vehicle=EntitySubPredicateMap(entity_type='minecraft:strider'),
                    ),
                    type='minecraft:entity_properties',
                ),
                distance=DistancePredicate(horizontal=MinMaxBounds(min=50.0)),
            ),
            trigger='minecraft:ride_entity_in_lava',
        ),
    },
    requirements=[['ride_entity_distance']],
    sends_telemetry_event=True,
)

ROOT = Advancement(
    display=RootAdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:red_nether_bricks'),
        title=TextObjectStruct2(translate='advancements.nether.root.title'),
        description=TextObjectStruct2(translate='advancements.nether.root.description'),
        show_toast=False,
        announce_to_chat=False,
        background='minecraft:gui/advancements/backgrounds/nether',
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

SUMMON_WITHER = Advancement(
    parent='minecraft:nether/get_wither_skull',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:nether_star'),
        title=TextObjectStruct2(translate='advancements.nether.summon_wither.title'),
        description=TextObjectStruct2(translate='advancements.nether.summon_wither.description'),
    ),
    criteria={
        'summoned': AdvancementCriterionSummonedEntity(
            conditions=SummonedEntityTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:wither'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:summoned_entity',
        ),
    },
    requirements=[['summoned']],
    sends_telemetry_event=True,
)

UNEASY_ALLIANCE = Advancement(
    parent='minecraft:nether/return_to_sender',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:ghast_tear'),
        title=TextObjectStruct2(translate='advancements.nether.uneasy_alliance.title'),
        description=TextObjectStruct2(translate='advancements.nether.uneasy_alliance.description'),
        frame=AdvancementFrame.CHALLENGE,
    ),
    criteria={
        'killed_ghast': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(
                        entity_type='minecraft:ghast',
                        location=LocationPredicate(dimension='minecraft:overworld'),
                    ),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
    },
    requirements=[['killed_ghast']],
    rewards=AdvancementRewards(experience=100),
    sends_telemetry_event=True,
)
