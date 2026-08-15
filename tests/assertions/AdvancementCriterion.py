# ~~~ WHAT ARE WE TESTING ~~~



# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::data::advancement::AdvancementCriterion
Local link to file: generated_symbols/data/advancement/AdvancementCriterion.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.data.advancement.trigger.BlockStateConditions import BlockStateConditions
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.DamagePredicate import DamagePredicate
    from generated_symbols.data.advancement.predicate.DamageSourcePredicate import DamageSourcePredicate
    from generated_symbols.data.advancement.predicate.DistancePredicate import DistancePredicate
    from generated_symbols.data.advancement.predicate.EntityEffectsPredicate import EntityEffectsPredicate
    from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate
    from generated_symbols.data.advancement.predicate.LocationPredicate import LocationPredicate
    from generated_symbols.data.advancement.trigger.AdvancementEntityPredicate import AdvancementEntityPredicate
    from generated_symbols.data.advancement.trigger.AdvancementLocationPredicate import AdvancementLocationPredicate
    from generated_symbols.data.advancement.trigger.ItemUesdOnLocationConditions import ItemUesdOnLocationConditions
    from generated_symbols.data.loot.LootTableListRef import LootTableListRef
    from generated_symbols.data.recipe.RecipeListRef import RecipeListRef
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds
    from generated_symbols.util.registry_ref.BlockListRef import BlockListRef
    from generated_symbols.world.component.predicate.PotionsPredicate import PotionsPredicate


@dataclass(kw_only=True)
class ConditionsStruct(PlayerConditions):
    location: AdvancementLocationPredicate | None = None  # Predicate context: Advancement Location.


type StateStructBlockStatesNone = dict[str, str]


@dataclass(kw_only=True)
class ConditionsStruct2(PlayerConditions):
    blocks: BlockListRef | None = None
    state: StateStructBlockStatesNone | None = None
    num_bees_inside: int | None = None  # Number of bees that were inside the bee nest/beehive before it was broken.
    item: ItemPredicate | None = None  # Item used to break the block.


@dataclass(kw_only=True)
class ConditionsStruct3(PlayerConditions):
    parent: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.
    partner: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.
    child: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.  Entity may not exist.


@dataclass(kw_only=True)
class ConditionsStruct4(PlayerConditions):
    potion: PotionsPredicate | None = None


@dataclass(kw_only=True)
class ConditionsStruct5(PlayerConditions):
    from_: Annotated[str, IdSpec(registry='dimension')] | None = None
    to: Annotated[str, IdSpec(registry='dimension')] | None = None


@dataclass(kw_only=True)
class ConditionsStruct6(PlayerConditions):
    victims: list[AdvancementEntityPredicate] | None = None  # Predicate context: Advancement Entity.  Evaluates to true if every predicate in the list matches some victims.


@dataclass(kw_only=True)
class ConditionsStruct7(PlayerConditions):
    level: MinMaxBounds[int] | int | None = None  # Tier of the updated beacon base.


@dataclass(kw_only=True)
class ConditionsStruct8(PlayerConditions):
    item: ItemPredicate | None = None


@dataclass(kw_only=True)
class ConditionsStruct9(PlayerConditions):
    recipes: RecipeListRef
    ingredients: Annotated[list[ItemPredicate], 'Length = 1-9 (both inclusive)'] | None = None


@dataclass(kw_only=True)
class ConditionsStruct10(PlayerConditions):
    zombie: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.
    villager: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.


@dataclass(kw_only=True)
class ConditionsStruct11(PlayerConditions):
    location: AdvancementLocationPredicate | None = None  # Predicate context: Block Use.


@dataclass(kw_only=True)
class ConditionsStruct12(PlayerConditions):
    effects: EntityEffectsPredicate | None = None
    source: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.  Entity may not exist.


@dataclass(kw_only=True)
class ConditionsStruct13(PlayerConditions):
    item: ItemPredicate | None = None
    levels: MinMaxBounds[int] | int | None = None


@dataclass(kw_only=True)
class ConditionsStruct14(BlockStateConditions, PlayerConditions):
    pass


@dataclass(kw_only=True)
class ConditionsStruct15(PlayerConditions):
    damage: DamagePredicate | None = None


@dataclass(kw_only=True)
class ConditionsStruct16(PlayerConditions):
    entity: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.
    killing_blow: DamageSourcePredicate | None = None


@dataclass(kw_only=True)
class ConditionsStruct17(PlayerConditions):
    start_position: LocationPredicate | None = None
    distance: DistancePredicate | None = None
    cause: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.  Entity may not exist.


@dataclass(kw_only=True)
class ConditionsStruct18(PlayerConditions):
    start_position: LocationPredicate | None = None  # Where the player started to travel.
    distance: DistancePredicate | None = None  # How far the player travels.


@dataclass(kw_only=True)
class ConditionsStruct19(PlayerConditions):
    entity: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.  Entity that was pulled. Or the hook itself if no entity was hooked.
    item: ItemPredicate | None = None  # Item that was caught.
    rod: ItemPredicate | None = None  # Fishing rod used.


@dataclass(kw_only=True)
class ConditionsStruct20:
    pass


@dataclass(kw_only=True)
class SlotsStruct:
    empty: MinMaxBounds[int] | int | None = None  # Amount of empty slots.
    occupied: MinMaxBounds[int] | int | None = None  # Amount of occupied slots.
    full: MinMaxBounds[int] | int | None = None  # Amount of slots that are a full stack.


@dataclass(kw_only=True)
class ConditionsStruct21(PlayerConditions):
    slots: SlotsStruct | None = None
    items: list[ItemPredicate] | None = None


@dataclass(kw_only=True)
class ConditionsStruct22(PlayerConditions):
    delta: MinMaxBounds[int] | int | None = None  # Change in durability (negative numbers are used to indicate a decrease in durability).
    durability: MinMaxBounds[int] | int | None = None  # The resulting durability.
    item: ItemPredicate | None = None  # The item before its durability changed.


@dataclass(kw_only=True)
class ConditionsStruct23(PlayerConditions):
    unique_entity_types: MinMaxBounds[int] | int | None = None  # How many different types of entities were killed.
    fired_from_weapon: ItemPredicate | None = None  # The weapon item that was used to fire the arrow.
    victims: list[AdvancementEntityPredicate] | None = None  # Predicate context: Advancement Entity.  Evaluates to true if every predicate in the list matches some victims.


@dataclass(kw_only=True)
class ConditionsStruct24(PlayerConditions):
    distance: DistancePredicate | None = None
    duration: MinMaxBounds[int] | int | None = None


@dataclass(kw_only=True)
class ConditionsStruct25(PlayerConditions):
    lightning: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.
    bystander: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.  Evaluates to false if no entities are nearby.


@dataclass(kw_only=True)
class ConditionsStruct26(PlayerConditions):
    start_position: LocationPredicate | None = None  # Where in the Overworld the player was when they travelled to the Nether.
    distance: DistancePredicate | None = None  # How far the player now is from the coordinate they started at in the Overworld before travelling.


@dataclass(kw_only=True)
class ConditionsStruct27(PlayerConditions):
    loot_tables: LootTableListRef


@dataclass(kw_only=True)
class ConditionsStruct28(PlayerConditions):
    damage: DamagePredicate | None = None
    entity: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.


@dataclass(kw_only=True)
class ConditionsStruct29(PlayerConditions):
    item: ItemPredicate | None = None
    entity: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.


@dataclass(kw_only=True)
class ConditionsStruct30(PlayerConditions):
    recipes: RecipeListRef


@dataclass(kw_only=True)
class ConditionsStruct31(PlayerConditions):
    item: ItemPredicate | None = None  # Crossbow that was used.


@dataclass(kw_only=True)
class ConditionsStruct32(PlayerConditions):
    count: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # Minimum mob count required.


@dataclass(kw_only=True)
class ConditionsStruct33(PlayerConditions):
    entity: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.


@dataclass(kw_only=True)
class ConditionsStruct34(PlayerConditions):
    projectile: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.
    signal_strength: MinMaxBounds[int] | int | None = None


@dataclass(kw_only=True)
class ConditionsStruct35(PlayerConditions):
    item: ItemPredicate | None = None
    entity: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.  Entity may not exist.


@dataclass(kw_only=True)
class ConditionsStruct36(PlayerConditions):
    distance: MinMaxBounds[float] | float | None = None  # Horizontal distance between the player and the stronghold.


@dataclass(kw_only=True)
class ConditionsStruct37(PlayerConditions):
    villager: AdvancementEntityPredicate | None = None  # Predicate context: Advancement Entity.
    item: ItemPredicate | None = None  # Item that was purchased.  `count` tag checks the item count from one trade, not the total amount traded for.


@dataclass(kw_only=True)
class AdvancementCriterionAllayDropItemOnBlock:
    trigger: Literal['minecraft:allay_drop_item_on_block']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ItemUesdOnLocationConditions | None = None


@dataclass(kw_only=True)
class AdvancementCriterionAnyBlockUse:
    trigger: Literal['minecraft:any_block_use']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct | None = None


@dataclass(kw_only=True)
class AdvancementCriterionAvoidVibration:
    trigger: Literal['minecraft:avoid_vibration']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: PlayerConditions | None = None


@dataclass(kw_only=True)
class AdvancementCriterionBeeNestDestroyed:
    trigger: Literal['minecraft:bee_nest_destroyed']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct2 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionBredAnimals:
    trigger: Literal['minecraft:bred_animals']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct3 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionBrewedPotion:
    trigger: Literal['minecraft:brewed_potion']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct4 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionChangedDimension:
    trigger: Literal['minecraft:changed_dimension']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct5 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionChanneledLightning:
    trigger: Literal['minecraft:channeled_lightning']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct6 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionConstructBeacon:
    trigger: Literal['minecraft:construct_beacon']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct7 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionConsumeItem:
    trigger: Literal['minecraft:consume_item']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct8 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionCrafterRecipeCrafted:
    trigger: Literal['minecraft:crafter_recipe_crafted']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct9


@dataclass(kw_only=True)
class AdvancementCriterionCuredZombieVillager:
    trigger: Literal['minecraft:cured_zombie_villager']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct10 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionDefaultBlockUse:
    trigger: Literal['minecraft:default_block_use']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct11 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionEffectsChanged:
    trigger: Literal['minecraft:effects_changed']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct12 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionEnchantedItem:
    trigger: Literal['minecraft:enchanted_item']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct13 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionEnterBlock:
    trigger: Literal['minecraft:enter_block']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct14 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionEntityHurtPlayer:
    trigger: Literal['minecraft:entity_hurt_player']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct15 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionEntityKilledPlayer:
    trigger: Literal['minecraft:entity_killed_player']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct16 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionFallAfterExplosion:
    trigger: Literal['minecraft:fall_after_explosion']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct17 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionFallFromHeight:
    trigger: Literal['minecraft:fall_from_height']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct18 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionFilledBucket:
    trigger: Literal['minecraft:filled_bucket']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct8 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionFishingRodHooked:
    trigger: Literal['minecraft:fishing_rod_hooked']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct19 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionHeroOfTheVillage:
    trigger: Literal['minecraft:hero_of_the_village']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: PlayerConditions | None = None


@dataclass(kw_only=True)
class AdvancementCriterionImpossible:
    trigger: Literal['minecraft:impossible']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct20 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionInventoryChanged:
    trigger: Literal['minecraft:inventory_changed']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct21 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionItemDurabilityChanged:
    trigger: Literal['minecraft:item_durability_changed']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct22 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionItemUsedOnBlock:
    trigger: Literal['minecraft:item_used_on_block']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ItemUesdOnLocationConditions | None = None


@dataclass(kw_only=True)
class AdvancementCriterionKillMobNearSculkCatalyst:
    trigger: Literal['minecraft:kill_mob_near_sculk_catalyst']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct16 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionKilledByArrow:
    trigger: Literal['minecraft:killed_by_arrow']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct23 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionKilledByCrossbow:
    trigger: Literal['minecraft:killed_by_crossbow']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct23 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionLevitation:
    trigger: Literal['minecraft:levitation']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct24 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionLightningStrike:
    trigger: Literal['minecraft:lightning_strike']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct25 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionLocation:
    trigger: Literal['minecraft:location']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: PlayerConditions | None = None


@dataclass(kw_only=True)
class AdvancementCriterionNetherTravel:
    trigger: Literal['minecraft:nether_travel']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct26 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionPlacedBlock:
    trigger: Literal['minecraft:placed_block']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ItemUesdOnLocationConditions | None = None


@dataclass(kw_only=True)
class AdvancementCriterionPlayerGeneratesContainerLoot:
    trigger: Literal['minecraft:player_generates_container_loot']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct27


@dataclass(kw_only=True)
class AdvancementCriterionPlayerHurtEntity:
    trigger: Literal['minecraft:player_hurt_entity']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct28 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionPlayerInteractedWithEntity:
    trigger: Literal['minecraft:player_interacted_with_entity']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct29 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionPlayerKilledEntity:
    trigger: Literal['minecraft:player_killed_entity']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct16 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionPlayerShearedEquipment:
    trigger: Literal['minecraft:player_sheared_equipment']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct29 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionRecipeCrafted:
    trigger: Literal['minecraft:recipe_crafted']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct9


@dataclass(kw_only=True)
class AdvancementCriterionRecipeUnlocked:
    trigger: Literal['minecraft:recipe_unlocked']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct30


@dataclass(kw_only=True)
class AdvancementCriterionRideEntityInLava:
    trigger: Literal['minecraft:ride_entity_in_lava']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct18 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionSafelyHarvestHoney:
    trigger: Literal['minecraft:safely_harvest_honey']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ItemUesdOnLocationConditions | None = None


@dataclass(kw_only=True)
class AdvancementCriterionShotCrossbow:
    trigger: Literal['minecraft:shot_crossbow']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct31 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionSleptInBed:
    trigger: Literal['minecraft:slept_in_bed']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: PlayerConditions | None = None


@dataclass(kw_only=True)
class AdvancementCriterionSlideDownBlock:
    trigger: Literal['minecraft:slide_down_block']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct14 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionSpearMobs:
    trigger: Literal['minecraft:spear_mobs']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct32 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionStartedRiding:
    trigger: Literal['minecraft:started_riding']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: PlayerConditions | None = None


@dataclass(kw_only=True)
class AdvancementCriterionSummonedEntity:
    trigger: Literal['minecraft:summoned_entity']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct33 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionTameAnimal:
    trigger: Literal['minecraft:tame_animal']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct33 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionTargetHit:
    trigger: Literal['minecraft:target_hit']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct34 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionThrownItemPickedUpByEntity:
    trigger: Literal['minecraft:thrown_item_picked_up_by_entity']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct35 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionThrownItemPickedUpByPlayer:
    trigger: Literal['minecraft:thrown_item_picked_up_by_player']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct35 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionTick:
    trigger: Literal['minecraft:tick']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: PlayerConditions | None = None


@dataclass(kw_only=True)
class AdvancementCriterionUsedEnderEye:
    trigger: Literal['minecraft:used_ender_eye']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct36 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionUsedTotem:
    trigger: Literal['minecraft:used_totem']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct8 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionUsingItem:
    trigger: Literal['minecraft:using_item']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct8 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionVillagerTrade:
    trigger: Literal['minecraft:villager_trade']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConditionsStruct37 | None = None


@dataclass(kw_only=True)
class AdvancementCriterionVoluntaryExile:
    trigger: Literal['minecraft:voluntary_exile']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: PlayerConditions | None = None


type AdvancementCriterion = AdvancementCriterionAllayDropItemOnBlock | AdvancementCriterionAnyBlockUse | AdvancementCriterionAvoidVibration | AdvancementCriterionBeeNestDestroyed | AdvancementCriterionBredAnimals | AdvancementCriterionBrewedPotion | AdvancementCriterionChangedDimension | AdvancementCriterionChanneledLightning | AdvancementCriterionConstructBeacon | AdvancementCriterionConsumeItem | AdvancementCriterionCrafterRecipeCrafted | AdvancementCriterionCuredZombieVillager | AdvancementCriterionDefaultBlockUse | AdvancementCriterionEffectsChanged | AdvancementCriterionEnchantedItem | AdvancementCriterionEnterBlock | AdvancementCriterionEntityHurtPlayer | AdvancementCriterionEntityKilledPlayer | AdvancementCriterionFallAfterExplosion | AdvancementCriterionFallFromHeight | AdvancementCriterionFilledBucket | AdvancementCriterionFishingRodHooked | AdvancementCriterionHeroOfTheVillage | AdvancementCriterionImpossible | AdvancementCriterionInventoryChanged | AdvancementCriterionItemDurabilityChanged | AdvancementCriterionItemUsedOnBlock | AdvancementCriterionKillMobNearSculkCatalyst | AdvancementCriterionKilledByArrow | AdvancementCriterionKilledByCrossbow | AdvancementCriterionLevitation | AdvancementCriterionLightningStrike | AdvancementCriterionLocation | AdvancementCriterionNetherTravel | AdvancementCriterionPlacedBlock | AdvancementCriterionPlayerGeneratesContainerLoot | AdvancementCriterionPlayerHurtEntity | AdvancementCriterionPlayerInteractedWithEntity | AdvancementCriterionPlayerKilledEntity | AdvancementCriterionPlayerShearedEquipment | AdvancementCriterionRecipeCrafted | AdvancementCriterionRecipeUnlocked | AdvancementCriterionRideEntityInLava | AdvancementCriterionSafelyHarvestHoney | AdvancementCriterionShotCrossbow | AdvancementCriterionSleptInBed | AdvancementCriterionSlideDownBlock | AdvancementCriterionSpearMobs | AdvancementCriterionStartedRiding | AdvancementCriterionSummonedEntity | AdvancementCriterionTameAnimal | AdvancementCriterionTargetHit | AdvancementCriterionThrownItemPickedUpByEntity | AdvancementCriterionThrownItemPickedUpByPlayer | AdvancementCriterionTick | AdvancementCriterionUsedEnderEye | AdvancementCriterionUsedTotem | AdvancementCriterionUsingItem | AdvancementCriterionVillagerTrade | AdvancementCriterionVoluntaryExile

