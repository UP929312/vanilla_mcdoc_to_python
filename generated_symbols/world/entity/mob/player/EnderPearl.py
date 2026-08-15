"""
Generated from symbols.json for ::java::world::entity::mob::player::EnderPearl
Local link to file: generated_symbols/world/entity/mob/player/EnderPearl.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.world.block.command_block.BaseCommandBlock import BaseCommandBlock
from generated_symbols.world.entity.BlockAttachedEntity import BlockAttachedEntity
from generated_symbols.world.entity.EntityBase import EntityBase
from generated_symbols.world.entity.boat.Boat import Boat
from generated_symbols.world.entity.display.DisplayBase import DisplayBase
from generated_symbols.world.entity.minecart.ContainerMinecart import ContainerMinecart
from generated_symbols.world.entity.minecart.Minecart import Minecart
from generated_symbols.world.entity.mob.AgeableMob import AgeableMob
from generated_symbols.world.entity.mob.LivingEntity import LivingEntity
from generated_symbols.world.entity.mob.MobBase import MobBase
from generated_symbols.world.entity.mob.NeutralMob import NeutralMob
from generated_symbols.world.entity.mob.breedable.Breedable import Breedable
from generated_symbols.world.entity.mob.breedable.horse.ChestedHorse import ChestedHorse
from generated_symbols.world.entity.mob.breedable.horse.HorseBase import HorseBase
from generated_symbols.world.entity.mob.breedable.horse.Llama import Llama
from generated_symbols.world.entity.mob.breedable.saddled.Saddled import Saddled
from generated_symbols.world.entity.mob.breedable.tamable.Tamable import Tamable
from generated_symbols.world.entity.mob.breedable.villager.VillagerBase import VillagerBase
from generated_symbols.world.entity.mob.fish.Fish import Fish
from generated_symbols.world.entity.mob.piglin.PiglinBase import PiglinBase
from generated_symbols.world.entity.mob.raider.RaiderBase import RaiderBase
from generated_symbols.world.entity.mob.slime.CubeMob import CubeMob
from generated_symbols.world.entity.mob.zombie.Zombie import Zombie
from generated_symbols.world.entity.projectile.ProjectileBase import ProjectileBase
from generated_symbols.world.entity.projectile.arrow.ArrowBase import ArrowBase
from generated_symbols.world.entity.projectile.fireball.AcceleratingProjectileBase import AcceleratingProjectileBase
from generated_symbols.world.entity.projectile.fireball.DespawnableProjectileBase import DespawnableProjectileBase
from generated_symbols.world.entity.projectile.fireball.FireballBase import FireballBase
from generated_symbols.world.entity.projectile.throwable.Throwable import Throwable
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.assets.model.ItemDisplayContext import ItemDisplayContext
    from generated_symbols.util.BlockState import BlockState as BlockState2
    from generated_symbols.util.DyeColorByte import DyeColorByte
    from generated_symbols.util.GlobalPos import GlobalPos
    from generated_symbols.util.avatar.HumanoidArm import HumanoidArm
    from generated_symbols.util.avatar.PlayerModelPart import PlayerModelPart
    from generated_symbols.util.avatar.Profile import Profile
    from generated_symbols.util.block_state.BlockState import BlockState
    from generated_symbols.util.color.DyeColor import DyeColor
    from generated_symbols.util.color.DyeColorByte import DyeColorByte as DyeColorByte2
    from generated_symbols.util.direction.DirectionByte import DirectionByte
    from generated_symbols.util.direction.HorizontalDirectionByte import HorizontalDirectionByte
    from generated_symbols.util.game_event.VibrationListener import VibrationListener
    from generated_symbols.util.particle.Particle import Particle
    from generated_symbols.util.slot.SlottedItem import SlottedItem
    from generated_symbols.util.text.Text import Text
    from generated_symbols.world.block.spawner.SpawnPotential import SpawnPotential
    from generated_symbols.world.block.spawner.SpawnerEntry import SpawnerEntry
    from generated_symbols.world.component.entity.FoxType import FoxType
    from generated_symbols.world.component.entity.MooshroomType import MooshroomType
    from generated_symbols.world.component.entity.SalmonType import SalmonType
    from generated_symbols.world.component.item.PotionContents import PotionContents
    from generated_symbols.world.component.item.SuspiciousStewEffect import SuspiciousStewEffect
    from generated_symbols.world.entity.AnyEntity import AnyEntity
    from generated_symbols.world.entity.display.TextAlignment import TextAlignment
    from generated_symbols.world.entity.interaction.Action import Action
    from generated_symbols.world.entity.mob.DropChances import DropChances
    from generated_symbols.world.entity.mob.EntityEquipment import EntityEquipment
    from generated_symbols.world.entity.mob.armor_stand.Pose import Pose
    from generated_symbols.world.entity.mob.breedable.armadillo.ArmadilloState import ArmadilloState
    from generated_symbols.world.entity.mob.breedable.axolotl.AxolotlVariantInt import AxolotlVariantInt
    from generated_symbols.world.entity.mob.breedable.horse.HorseVariantAndMarkings import HorseVariantAndMarkings
    from generated_symbols.world.entity.mob.breedable.horse.LlamaVariantInt import LlamaVariantInt
    from generated_symbols.world.entity.mob.breedable.panda.Gene import Gene
    from generated_symbols.world.entity.mob.breedable.rabbit.RabbitType import RabbitType
    from generated_symbols.world.entity.mob.breedable.tamable.ParrotVariantInt import ParrotVariantInt
    from generated_symbols.world.entity.mob.breedable.villager.Offers import Offers
    from generated_symbols.world.entity.mob.breedable.villager.PlayerReputationPart import PlayerReputationPart
    from generated_symbols.world.entity.mob.breedable.villager.VillagerData import VillagerData
    from generated_symbols.world.entity.mob.copper_golem.WeatherState import WeatherState
    from generated_symbols.world.entity.mob.ender_dragon.DragonPhase import DragonPhase
    from generated_symbols.world.entity.mob.fish.PuffState import PuffState
    from generated_symbols.world.entity.mob.mannequin.MannequinPose import MannequinPose
    from generated_symbols.world.entity.mob.player.Abilities import Abilities
    from generated_symbols.world.entity.mob.player.Gamemode import Gamemode
    from generated_symbols.world.entity.mob.player.PlayerEquipment import PlayerEquipment
    from generated_symbols.world.entity.mob.player.PlayerSlot import PlayerSlot
    from generated_symbols.world.entity.mob.player.RecipeBook import RecipeBook
    from generated_symbols.world.entity.mob.player.Respawn import Respawn
    from generated_symbols.world.entity.mob.player.RootVehicle import RootVehicle
    from generated_symbols.world.entity.mob.player.WardenSpawnTracker import WardenSpawnTracker
    from generated_symbols.world.entity.mob.shulker.ShulkerColor import ShulkerColor
    from generated_symbols.world.entity.mob.warden.AngerManagement import AngerManagement
    from generated_symbols.world.entity.projectile.shulker_bullet.BulletTarget import BulletTarget
    from generated_symbols.world.item.ItemStack import ItemStack


@dataclass(kw_only=True)
class LeashStruct:
    UUID: tuple[int, int, int, int] | None = None


@dataclass(kw_only=True)
class ItemsStruct:
    pass


@dataclass(kw_only=True)
class TileEntityDataStruct:
    pass


@dataclass(kw_only=True)
class EnderPearlAcaciaBoat(EntityBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:acacia_boat']  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlAcaciaChestBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:acacia_chest_boat']  # The ID of this entity. Not present on player entities.
    LootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that will populate this chest boat.
    LootTableSeed: int | None = None  # Seed of the loot table.
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`26` | both inclusive']]], 'Length = 0-27 (both inclusive)'] | None = None  # Slots from 0 to 26.


@dataclass(kw_only=True)
class EnderPearlAllay(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:allay']  # The ID of this entity. Not present on player entities.
    DuplicationCooldown: int | None = None  # Ticks until the allay can duplicate. This is set to 6000 game ticks (5 minutes) when the allay duplicates.
    Inventory: tuple[ItemStack] | None = None  # Items it has picked up. Note that the item given by the player is in the allay's `HandItems[0]` tag, not here.
    listener: VibrationListener | None = None  # Vibration game event listener.


@dataclass(kw_only=True)
class EnderPearlAreaEffectCloud(EntityBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:area_effect_cloud']  # The ID of this entity. Not present on player entities.
    Age: int | None = None  # Number of ticks it has existed. Controls when it will despawn; when greater than `Duration + WaitTime`.
    Color: int | None = None  # Color of the particles. calculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive
    Duration: int | None = None  # Maximum number of ticks until it will disappear after `WaitTime` is done
    ReapplicationDelay: int | None = None  # Number of ticks until the effects are reapplied.
    WaitTime: int | None = None  # Number of ticks until it appears.
    DurationOnUse: int | None = None  # Amount the duration changes when it is active.
    Owner: tuple[int, int, int, int] | None = None
    Radius: float | None = None  # Radius of the particles & effect applications.
    RadiusOnUse: float | None = None  # Change in the radius when it is used.
    RadiusPerTick: float | None = None  # Change in the radius per tick.
    custom_particle: Particle | None = None  # If present, the particle that the area effect cloud displays instead of the default `entity_effect` particle based on the potion contents.
    potion_contents: PotionContents | Annotated[str, IdSpec(registry='potion')] | None = None
    potion_duration_scale: float | None = None  # The duration of the potion effect applied is scaled by this factor. Defaults to `1`. Will be `0.25` when throwing lingering potions.


@dataclass(kw_only=True)
class EnderPearlArmadillo(Breedable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:armadillo']  # The ID of this entity. Not present on player entities.
    state: ArmadilloState | None = None
    scute_time: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None


@dataclass(kw_only=True)
class EnderPearlArmorStand(LivingEntity):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:armor_stand']  # The ID of this entity. Not present on player entities.
    equipment: EntityEquipment | None = None  # The equipment items of the armor stand.
    Invisible: bool | None = None  # Whether it should be invisible.
    Marker: bool | None = None  # Whether it has no hitbox.
    NoBasePlate: bool | None = None  # Whether it should have a no base plate.
    ShowArms: bool | None = None  # Whether it should show its arms.
    Small: bool | None = None  # Whether it is small.
    DisabledSlots: int | None = None  # A bitfield of the slots that cannot be used.
    Pose: Pose | None = None  # Body part rotations.


@dataclass(kw_only=True)
class EnderPearlArrow(ArrowBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:arrow']  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlAxolotl(Breedable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:axolotl']  # The ID of this entity. Not present on player entities.
    Variant: AxolotlVariantInt | None = None  # The variant of the axolotl.
    FromBucket: bool | None = None  # If this axolotl was released from a bucket.


@dataclass(kw_only=True)
class EnderPearlBambooChestRaft(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:bamboo_chest_raft']  # The ID of this entity. Not present on player entities.
    LootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that will populate this chest boat.
    LootTableSeed: int | None = None  # Seed of the loot table.
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`26` | both inclusive']]], 'Length = 0-27 (both inclusive)'] | None = None  # Slots from 0 to 26.


@dataclass(kw_only=True)
class EnderPearlBambooRaft(EntityBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:bamboo_raft']  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlBat(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:bat']  # The ID of this entity. Not present on player entities.
    BatFlags: bool | None = None  # Whether it is upside down.


@dataclass(kw_only=True)
class EnderPearlBee(Breedable, NeutralMob):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:bee']  # The ID of this entity. Not present on player entities.
    hive_pos: tuple[int, int, int] | None = None
    flower_pos: tuple[int, int, int] | None = None  # Position of the flower the bee is circling
    HasNectar: bool | None = None  # Whether the bee has nectar.
    HasStung: bool | None = None  # Whether the bee has stung an entity.
    TicksSincePollination: int | None = None  # Ticks since the bee has pollinated a crop.
    CannotEnterHiveTicks: int | None = None  # Ticks until the bee can enter its hive.
    CropsGrownSincePollination: int | None = None  # Crops grown since the bee has gathered nectar.
    Anger: int | None = None  # Ticks the bee will be angry for.
    HurtBy: tuple[int, int, int, int] | None = None  # Player that has attacked the bee.


@dataclass(kw_only=True)
class EnderPearlBirchBoat(EntityBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:birch_boat']  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlBirchChestBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:birch_chest_boat']  # The ID of this entity. Not present on player entities.
    LootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that will populate this chest boat.
    LootTableSeed: int | None = None  # Seed of the loot table.
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`26` | both inclusive']]], 'Length = 0-27 (both inclusive)'] | None = None  # Slots from 0 to 26.


@dataclass(kw_only=True)
class EnderPearlBlaze(LivingEntity):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:blaze']  # The ID of this entity. Not present on player entities.
    equipment: EntityEquipment | None = None  # The equipment items of the mob, such as armor or weapons.
    drop_chances: DropChances | None = None  # Chances of the mob dropping an equipment slot on death.
    DeathLootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that is dropped when the mob dies.
    DeathLootTableSeed: int | None = None  # Seed for generating the death loot table.
    CanPickUpLoot: bool | None = None  # Whether it can pick up loot.
    PersistenceRequired: bool | None = None  # Whether it should not despawn naturally.
    LeftHanded: bool | None = None  # Whether it is left handed.
    NoAI: bool | None = None  # Whether it should have an AI.
    leash: tuple[int, int, int] | LeashStruct | None = None  # What the leash is attached to.
    home_radius: int | None = None  # Defaults to -1, which represents "no home".
    home_pos: tuple[int, int, int] | None = None  # This field will be discarded if `home_radius` is less than 0.


@dataclass(kw_only=True)
class EnderPearlBlockDisplay(DisplayBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:block_display']  # The ID of this entity. Not present on player entities.
    block_state: BlockState | None = None  # Block state to display. Can display most block entities (eg. Chests, Beds, Furnaces, etc).  Does not display specially rendered block entities (eg. The bell in a bell block, an end gateway, the book on an enchantment table, a banner, a sign, etc).


@dataclass(kw_only=True)
class EnderPearlBoat(EntityBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:boat']  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlBogged(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:bogged']  # The ID of this entity. Not present on player entities.
    sheared: bool | None = None  # Whether the mushrooms on this bogged have been sheared.


@dataclass(kw_only=True)
class EnderPearlBreeze(LivingEntity):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:breeze']  # The ID of this entity. Not present on player entities.
    equipment: EntityEquipment | None = None  # The equipment items of the mob, such as armor or weapons.
    drop_chances: DropChances | None = None  # Chances of the mob dropping an equipment slot on death.
    DeathLootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that is dropped when the mob dies.
    DeathLootTableSeed: int | None = None  # Seed for generating the death loot table.
    CanPickUpLoot: bool | None = None  # Whether it can pick up loot.
    PersistenceRequired: bool | None = None  # Whether it should not despawn naturally.
    LeftHanded: bool | None = None  # Whether it is left handed.
    NoAI: bool | None = None  # Whether it should have an AI.
    leash: tuple[int, int, int] | LeashStruct | None = None  # What the leash is attached to.
    home_radius: int | None = None  # Defaults to -1, which represents "no home".
    home_pos: tuple[int, int, int] | None = None  # This field will be discarded if `home_radius` is less than 0.


@dataclass(kw_only=True)
class EnderPearlBreezeWindCharge(ProjectileBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:breeze_wind_charge']  # The ID of this entity. Not present on player entities.
    acceleration_power: float | None = None


@dataclass(kw_only=True)
class EnderPearlCamel(HorseBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:camel']  # The ID of this entity. Not present on player entities.
    IsSitting: bool | None = None  # Whether it is sitting.
    LastPoseTick: int | None = None  # The tick when it started changing its pose.


@dataclass(kw_only=True)
class EnderPearlCamelHusk(HorseBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:camel_husk']  # The ID of this entity. Not present on player entities.
    IsSitting: bool | None = None  # Whether it is sitting.
    LastPoseTick: int | None = None  # The tick when it started changing its pose.


@dataclass(kw_only=True)
class EnderPearlCat(Tamable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:cat']  # The ID of this entity. Not present on player entities.
    CollarColor: DyeColorByte | None = None  # Collar color, present for stray cats. Defaults to 14 (red).
    variant: Annotated[str, IdSpec(registry='cat_variant')] | None = None
    sound_variant: Annotated[str, IdSpec(registry='cat_sound_variant')] | None = None


@dataclass(kw_only=True)
class EnderPearlCaveSpider(LivingEntity):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:cave_spider']  # The ID of this entity. Not present on player entities.
    equipment: EntityEquipment | None = None  # The equipment items of the mob, such as armor or weapons.
    drop_chances: DropChances | None = None  # Chances of the mob dropping an equipment slot on death.
    DeathLootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that is dropped when the mob dies.
    DeathLootTableSeed: int | None = None  # Seed for generating the death loot table.
    CanPickUpLoot: bool | None = None  # Whether it can pick up loot.
    PersistenceRequired: bool | None = None  # Whether it should not despawn naturally.
    LeftHanded: bool | None = None  # Whether it is left handed.
    NoAI: bool | None = None  # Whether it should have an AI.
    leash: tuple[int, int, int] | LeashStruct | None = None  # What the leash is attached to.
    home_radius: int | None = None  # Defaults to -1, which represents "no home".
    home_pos: tuple[int, int, int] | None = None  # This field will be discarded if `home_radius` is less than 0.


@dataclass(kw_only=True)
class EnderPearlCherryBoat(EntityBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:cherry_boat']  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlCherryChestBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:cherry_chest_boat']  # The ID of this entity. Not present on player entities.
    LootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that will populate this chest boat.
    LootTableSeed: int | None = None  # Seed of the loot table.
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`26` | both inclusive']]], 'Length = 0-27 (both inclusive)'] | None = None  # Slots from 0 to 26.


@dataclass(kw_only=True)
class EnderPearlChestBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:chest_boat']  # The ID of this entity. Not present on player entities.
    LootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that will populate this chest boat.
    LootTableSeed: int | None = None  # Seed of the loot table.
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`26` | both inclusive']]], 'Length = 0-27 (both inclusive)'] | None = None  # Slots from 0 to 26.


@dataclass(kw_only=True)
class EnderPearlChestMinecart(ContainerMinecart, Minecart):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:chest_minecart']  # The ID of this entity. Not present on player entities.
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`26` | both inclusive']]], 'Length = 0-27 (both inclusive)'] | None = None  # Slots from 0 to 26.


@dataclass(kw_only=True)
class EnderPearlChicken(Breedable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:chicken']  # The ID of this entity. Not present on player entities.
    IsChickenJockey: bool | None = None  # Whether it is from a chicken jockey. If true it will despawn and will drop more experience.
    EggLayTime: int | None = None  # Time until it lays another egg.
    variant: Annotated[str, IdSpec(registry='chicken_variant')] | None = None
    sound_variant: Annotated[str, IdSpec(registry='chicken_sound_variant')] | None = None


@dataclass(kw_only=True)
class EnderPearlCod(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:cod']  # The ID of this entity. Not present on player entities.
    FromBucket: bool | None = None  # If it was released from a bucket.


@dataclass(kw_only=True)
class EnderPearlCommandBlockMinecart(BaseCommandBlock, Minecart):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:command_block_minecart']  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlCopperGolem(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:copper_golem']  # The ID of this entity. Not present on player entities.
    next_weather_age: Annotated[int, 'Range | Min `-2` and above | inclusive'] | None = None  # Gametime in ticks when the copper golem oxidizes.  `-2` represents "waxed"  `-1` will be replaced with a random time between 504000 and 552000 ticks later
    weather_state: WeatherState | None = None


@dataclass(kw_only=True)
class EnderPearlCow(Breedable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:cow']  # The ID of this entity. Not present on player entities.
    variant: Annotated[str, IdSpec(registry='cow_variant')] | None = None
    sound_variant: Annotated[str, IdSpec(registry='cow_sound_variant')] | None = None


@dataclass(kw_only=True)
class EnderPearlCreaking(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:creaking']  # The ID of this entity. Not present on player entities.
    home_pos: tuple[int, int, int] | None = None  # The creaking heart block that this is linked to.


@dataclass(kw_only=True)
class EnderPearlCreakingTransient(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:creaking_transient']  # The ID of this entity. Not present on player entities.
    home_pos: tuple[int, int, int] | None = None  # The creaking heart block that this is linked to.


@dataclass(kw_only=True)
class EnderPearlCreeper(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:creeper']  # The ID of this entity. Not present on player entities.
    powered: bool | None = None  # Whether it is being struck by lightning.
    ExplosionRadius: int | None = None  # Radius of the explosion.
    Fuse: int | None = None  # Ticks until it explodes.
    ignited: bool | None = None  # Whether it was lit with flint and steel.


@dataclass(kw_only=True)
class EnderPearlCushion(BlockAttachedEntity):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:cushion']  # The ID of this entity. Not present on player entities.
    color: DyeColor | None = None


@dataclass(kw_only=True)
class EnderPearlDarkOakBoat(EntityBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:dark_oak_boat']  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlDarkOakChestBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:dark_oak_chest_boat']  # The ID of this entity. Not present on player entities.
    LootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that will populate this chest boat.
    LootTableSeed: int | None = None  # Seed of the loot table.
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`26` | both inclusive']]], 'Length = 0-27 (both inclusive)'] | None = None  # Slots from 0 to 26.


@dataclass(kw_only=True)
class EnderPearlDolphin(AgeableMob, MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:dolphin']  # The ID of this entity. Not present on player entities.
    GotFish: bool | None = None  # Whether it has gotten fish from a player.
    Moistness: int | None = None  # Moistness level of the dolphin. Set to 2400 when the dolphin is in water or rain, otherwise decreases by 1 every tick. The dolphin takes damage when level is at 0 or below.


@dataclass(kw_only=True)
class EnderPearlDonkey(HorseBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:donkey']  # The ID of this entity. Not present on player entities.
    ChestedHorse: bool | None = None  # Whether it has a chest.
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`14` | both inclusive']] | ItemsStruct], 'Length = 0-15 (both inclusive)'] | None = None  # Slots from 0 to 14.


@dataclass(kw_only=True)
class EnderPearlDragonFireball(AcceleratingProjectileBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:dragon_fireball']  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlDrowned(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:drowned']  # The ID of this entity. Not present on player entities.
    IsBaby: bool | None = None  # Whether it is a baby.
    CanBreakDoors: bool | None = None  # Whether it can break doors.
    DrownedConversionTime: int | None = None  # Ticks until it converts.
    InWaterTime: int | None = None  # Ticks it has been in the water.


@dataclass(kw_only=True)
class EnderPearlEgg(Throwable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:egg']  # The ID of this entity. Not present on player entities.
    Item: ItemStack | None = None  # Item representation of the projectile.


@dataclass(kw_only=True)
class EnderPearlElderGuardian(LivingEntity):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:elder_guardian']  # The ID of this entity. Not present on player entities.
    equipment: EntityEquipment | None = None  # The equipment items of the mob, such as armor or weapons.
    drop_chances: DropChances | None = None  # Chances of the mob dropping an equipment slot on death.
    DeathLootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that is dropped when the mob dies.
    DeathLootTableSeed: int | None = None  # Seed for generating the death loot table.
    CanPickUpLoot: bool | None = None  # Whether it can pick up loot.
    PersistenceRequired: bool | None = None  # Whether it should not despawn naturally.
    LeftHanded: bool | None = None  # Whether it is left handed.
    NoAI: bool | None = None  # Whether it should have an AI.
    leash: tuple[int, int, int] | LeashStruct | None = None  # What the leash is attached to.
    home_radius: int | None = None  # Defaults to -1, which represents "no home".
    home_pos: tuple[int, int, int] | None = None  # This field will be discarded if `home_radius` is less than 0.


@dataclass(kw_only=True)
class EnderPearlEndCrystal(EntityBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:end_crystal']  # The ID of this entity. Not present on player entities.
    ShowBottom: bool | None = None  # Whether to show the base of the end crystal.
    beam_target: tuple[int, int, int] | None = None  # Coordinates that the beam is pointing to


@dataclass(kw_only=True)
class EnderPearlEnderDragon(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:ender_dragon']  # The ID of this entity. Not present on player entities.
    DragonPhase: DragonPhase | None = None  # Fighting phase it is in.


@dataclass(kw_only=True)
class EnderPearlEnderPearl(Throwable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:ender_pearl']  # The ID of this entity. Not present on player entities.
    Item: ItemStack | None = None  # Item representation of the projectile.


@dataclass(kw_only=True)
class EnderPearlEnderman(MobBase, NeutralMob):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:enderman']  # The ID of this entity. Not present on player entities.
    carriedBlockState: BlockState2 | None = None  # Block it is carrying.


@dataclass(kw_only=True)
class EnderPearlEndermite(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:endermite']  # The ID of this entity. Not present on player entities.
    Lifetime: int | None = None  # How long it has existed.
    PlayerSpawned: bool | None = None  # Whether enderman should attack it.


@dataclass(kw_only=True)
class EnderPearlEvoker(RaiderBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:evoker']  # The ID of this entity. Not present on player entities.
    SpellTicks: int | None = None  # Ticks until the raider can cast its spell.


@dataclass(kw_only=True)
class EnderPearlEvokerFangs(EntityBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:evoker_fangs']  # The ID of this entity. Not present on player entities.
    Warmup: int | None = None  # Ticks until the fangs pop out of the ground.
    Owner: tuple[int, int, int, int] | None = None


@dataclass(kw_only=True)
class EnderPearlExperienceBottle(Throwable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:experience_bottle']  # The ID of this entity. Not present on player entities.
    Item: ItemStack | None = None  # Item representation of the projectile.


@dataclass(kw_only=True)
class EnderPearlExperienceOrb(EntityBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:experience_orb']  # The ID of this entity. Not present on player entities.
    Age: int | None = None  # Ticks that it has existed.
    Health: int | None = None
    Value: int | None = None  # Amount of experience it will give.
    Count: int | None = None  # Remaining number of times that the orb can be picked up. When the orb is picked up, the value decreases by 1. When multiple orbs are merged, their values are added up to result orb. When the value reaches 0, the orb is depleted.


@dataclass(kw_only=True)
class EnderPearlEyeOfEnder(EntityBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:eye_of_ender']  # The ID of this entity. Not present on player entities.
    Item: ItemStack | None = None  # Item to render as.


@dataclass(kw_only=True)
class EnderPearlFallingBlock(EntityBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:falling_block']  # The ID of this entity. Not present on player entities.
    TileEntityData: TileEntityDataStruct | None = None  # NBT data for the placed block.
    BlockState: BlockState2 | None = None  # Block state for the placed block. Defaults to sand.
    Time: int | None = None  # Ticks it has existed.
    DropItem: bool | None = None  # Whether it should drop as a block when destroyed.
    HurtEntities: bool | None = None  # Whether this it should hurt entities.
    FallHurtMax: int | None = None  # Maximum damage it should deal.
    FallHurtAmount: float | None = None  # Damage multiplier.
    CancelDrop: bool | None = None  # Whether the block should be destroyed instead of placed after landing on a solid block. When `true`, the block is not dropped as an item, even if the DropItem tag is set to `true`. However, if the entity is deleted due to its Time value being too high, this tag is ignored and an item is dropped depending on the `DropItem` tag. Defaults to `1` for falling suspicious sand and suspicious gravel, and `0` for the other vanilla falling blocks and any summoned falling block.


@dataclass(kw_only=True)
class EnderPearlFireball(FireballBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:fireball']  # The ID of this entity. Not present on player entities.
    ExplosionPower: int | None = None  # Explosion radius.


@dataclass(kw_only=True)
class EnderPearlFireworkRocket(ProjectileBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:firework_rocket']  # The ID of this entity. Not present on player entities.
    Life: int | None = None  # Ticks it has existed.
    LifeTime: int | None = None  # Ticks it will exist.
    ShotAtAngle: bool | None = None  # Whether it should move at an angle.
    FireworksItem: ItemStack | None = None


@dataclass(kw_only=True)
class EnderPearlFox(Breedable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:fox']  # The ID of this entity. Not present on player entities.
    Trusted: list[tuple[int, int, int, int]] | None = None  # List of trusted players.
    Sleeping: bool | None = None  # Whether it is sleeping.
    Type: FoxType | None = None  # The type of fox.
    Sitting: bool | None = None  # Whether it is sitting.
    Crouching: bool | None = None  # Whether it is crouching.


@dataclass(kw_only=True)
class EnderPearlFrog(Breedable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:frog']  # The ID of this entity. Not present on player entities.
    variant: Annotated[str, IdSpec(registry='frog_variant')] | None = None


@dataclass(kw_only=True)
class EnderPearlFurnaceMinecart(Minecart):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:furnace_minecart']  # The ID of this entity. Not present on player entities.
    PushX: float | None = None  # Acceleration in x axis.
    PushZ: float | None = None  # Acceleration in z axis.
    Fuel: int | None = None  # Ticks until the fuel runs out.


@dataclass(kw_only=True)
class EnderPearlGhast(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:ghast']  # The ID of this entity. Not present on player entities.
    ExplosionPower: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # Explosion radius of fireballs that are shot from it.


@dataclass(kw_only=True)
class EnderPearlGiant(LivingEntity):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:giant']  # The ID of this entity. Not present on player entities.
    equipment: EntityEquipment | None = None  # The equipment items of the mob, such as armor or weapons.
    drop_chances: DropChances | None = None  # Chances of the mob dropping an equipment slot on death.
    DeathLootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that is dropped when the mob dies.
    DeathLootTableSeed: int | None = None  # Seed for generating the death loot table.
    CanPickUpLoot: bool | None = None  # Whether it can pick up loot.
    PersistenceRequired: bool | None = None  # Whether it should not despawn naturally.
    LeftHanded: bool | None = None  # Whether it is left handed.
    NoAI: bool | None = None  # Whether it should have an AI.
    leash: tuple[int, int, int] | LeashStruct | None = None  # What the leash is attached to.
    home_radius: int | None = None  # Defaults to -1, which represents "no home".
    home_pos: tuple[int, int, int] | None = None  # This field will be discarded if `home_radius` is less than 0.


@dataclass(kw_only=True)
class EnderPearlGlowItemFrame(BlockAttachedEntity):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:glow_item_frame']  # The ID of this entity. Not present on player entities.
    Facing: DirectionByte | None = None  # Direction it is facing.
    Item: ItemStack | None = None
    ItemDropChance: float | None = None  # Chance the item has to drop.
    ItemRotation: Annotated[int, 'Range | `0`-`7` | both inclusive'] | None = None  # Rotation of the item.
    Invisible: bool | None = None  # Whether the item frame should be invisible. The item inside the frame is not effected.
    Fixed: bool | None = None  # Whether the item frame should not be able to be broken and should disallow the item to be moved.


@dataclass(kw_only=True)
class EnderPearlGlowSquid(AgeableMob, MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:glow_squid']  # The ID of this entity. Not present on player entities.
    DarkTicksRemaining: int | None = None  # Ticks that it will wait before glowing.


@dataclass(kw_only=True)
class EnderPearlGoat(Breedable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:goat']  # The ID of this entity. Not present on player entities.
    HasLeftHorn: bool | None = None  # Whether it has its left horn.
    HasRightHorn: bool | None = None  # Whether it has its right horn.
    IsScreamingGoat: bool | None = None  # Whether it is a screaming goat.


@dataclass(kw_only=True)
class EnderPearlGuardian(LivingEntity):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:guardian']  # The ID of this entity. Not present on player entities.
    equipment: EntityEquipment | None = None  # The equipment items of the mob, such as armor or weapons.
    drop_chances: DropChances | None = None  # Chances of the mob dropping an equipment slot on death.
    DeathLootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that is dropped when the mob dies.
    DeathLootTableSeed: int | None = None  # Seed for generating the death loot table.
    CanPickUpLoot: bool | None = None  # Whether it can pick up loot.
    PersistenceRequired: bool | None = None  # Whether it should not despawn naturally.
    LeftHanded: bool | None = None  # Whether it is left handed.
    NoAI: bool | None = None  # Whether it should have an AI.
    leash: tuple[int, int, int] | LeashStruct | None = None  # What the leash is attached to.
    home_radius: int | None = None  # Defaults to -1, which represents "no home".
    home_pos: tuple[int, int, int] | None = None  # This field will be discarded if `home_radius` is less than 0.


@dataclass(kw_only=True)
class EnderPearlHappyGhast(AgeableMob, MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:happy_ghast']  # The ID of this entity. Not present on player entities.
    still_timeout: int | None = None


@dataclass(kw_only=True)
class EnderPearlHoglin(Breedable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:hoglin']  # The ID of this entity. Not present on player entities.
    IsImmuneToZombification: bool | None = None  # Whether it will not transform to a zoglin when it is in the Overword.
    CannotBeHunted: bool | None = None  # Whether it cannot be hunted by piglins
    TimeInOverworld: int | None = None  # The number of ticks it has been in the overworld.


@dataclass(kw_only=True)
class EnderPearlHopperMinecart(ContainerMinecart, Minecart):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:hopper_minecart']  # The ID of this entity. Not present on player entities.
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`4` | both inclusive']]], 'Length = 0-5 (both inclusive)'] | None = None  # Slots from 0 to 4.
    TransferCooldown: int | None = None  # Ticks until an item can be transferred.
    Enabled: bool | None = None  # Whether it should pick up items.


@dataclass(kw_only=True)
class EnderPearlHorse(HorseBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:horse']  # The ID of this entity. Not present on player entities.
    Variant: HorseVariantAndMarkings | None = None  # Variant of the horse. Stored as `baseColor | (markings << 8)`.


@dataclass(kw_only=True)
class EnderPearlHusk(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:husk']  # The ID of this entity. Not present on player entities.
    IsBaby: bool | None = None  # Whether it is a baby.
    CanBreakDoors: bool | None = None  # Whether it can break doors.
    DrownedConversionTime: int | None = None  # Ticks until it converts.
    InWaterTime: int | None = None  # Ticks it has been in the water.


@dataclass(kw_only=True)
class EnderPearlIllusioner(RaiderBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:illusioner']  # The ID of this entity. Not present on player entities.
    SpellTicks: int | None = None  # Ticks until the raider can cast its spell.


@dataclass(kw_only=True)
class EnderPearlInteraction(EntityBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:interaction']  # The ID of this entity. Not present on player entities.
    width: float | None = None  # Cube hitbox width centered on the entity. Negative values are effectively `| x |`.
    height: float | None = None  # Cube hitbox height stretching up from the entity position. Negative values stretch the hitbox down.
    response: bool | None = None  # Whether an action should trigger a response. Defaults to false. Response: Attack - When true, the default attack sound is played. Interaction - When true, the player's arm swings.
    attack: Action | None = None  # Record of last attack (left click) event, can be updated every tick (no invulnerability frames).
    interaction: Action | None = None  # Record of last interaction (use; right click) event, can be updated every tick, if the player is holding the key it updates every 3 ticks.


@dataclass(kw_only=True)
class EnderPearlIronGolem(MobBase, NeutralMob):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:iron_golem']  # The ID of this entity. Not present on player entities.
    PlayerCreated: bool | None = None  # Whether a player created it.


@dataclass(kw_only=True)
class EnderPearlItem(EntityBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:item']  # The ID of this entity. Not present on player entities.
    Age: int | None = None  # Ticks it has existed.
    Health: int | None = None
    PickupDelay: int | None = None  # Ticks until an entity can pick up this item.
    Owner: tuple[int, int, int, int] | None = None  # Only this entity can pick up the item.
    Thrower: tuple[int, int, int, int] | None = None  # Player who threw the item. Can be set and/or changed to any entity.
    Item: ItemStack | None = None


@dataclass(kw_only=True)
class EnderPearlItemDisplay(DisplayBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:item_display']  # The ID of this entity. Not present on player entities.
    item: ItemStack | None = None  # Item stack to display.
    item_display: ItemDisplayContext | None = None  # Describes item model transform applied to item (as defined in the `display` section in model JSON). Defaults to `fixed`.


@dataclass(kw_only=True)
class EnderPearlItemFrame(BlockAttachedEntity):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:item_frame']  # The ID of this entity. Not present on player entities.
    Facing: DirectionByte | None = None  # Direction it is facing.
    Item: ItemStack | None = None
    ItemDropChance: float | None = None  # Chance the item has to drop.
    ItemRotation: Annotated[int, 'Range | `0`-`7` | both inclusive'] | None = None  # Rotation of the item.
    Invisible: bool | None = None  # Whether the item frame should be invisible. The item inside the frame is not effected.
    Fixed: bool | None = None  # Whether the item frame should not be able to be broken and should disallow the item to be moved.


@dataclass(kw_only=True)
class EnderPearlJungleBoat(EntityBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:jungle_boat']  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlJungleChestBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:jungle_chest_boat']  # The ID of this entity. Not present on player entities.
    LootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that will populate this chest boat.
    LootTableSeed: int | None = None  # Seed of the loot table.
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`26` | both inclusive']]], 'Length = 0-27 (both inclusive)'] | None = None  # Slots from 0 to 26.


@dataclass(kw_only=True)
class EnderPearlLeashKnot(EntityBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:leash_knot']  # The ID of this entity. Not present on player entities.
    block_pos: tuple[int, int, int] | None = None


@dataclass(kw_only=True)
class EnderPearlLingeringPotion(Throwable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:lingering_potion']  # The ID of this entity. Not present on player entities.
    Item: ItemStack | None = None  # Item representation of the potion.


@dataclass(kw_only=True)
class EnderPearlLlama(ChestedHorse):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:llama']  # The ID of this entity. Not present on player entities.
    Strength: Annotated[int, 'Range | `1`-`5` | both inclusive'] | None = None  # Determines both the number of items it can carry and how likely it is for wolves to run away.
    Variant: LlamaVariantInt | None = None  # The variant of this llama.


@dataclass(kw_only=True)
class EnderPearlLlamaSpit(ProjectileBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:llama_spit']  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlMagmaCube(CubeMob, MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:magma_cube']  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlMangroveBoat(EntityBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:mangrove_boat']  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlMangroveChestBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:mangrove_chest_boat']  # The ID of this entity. Not present on player entities.
    LootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that will populate this chest boat.
    LootTableSeed: int | None = None  # Seed of the loot table.
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`26` | both inclusive']]], 'Length = 0-27 (both inclusive)'] | None = None  # Slots from 0 to 26.


@dataclass(kw_only=True)
class EnderPearlMannequin(LivingEntity):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:mannequin']  # The ID of this entity. Not present on player entities.
    profile: Profile | None = None
    hidden_layers: list[PlayerModelPart] | None = None
    main_hand: HumanoidArm | None = None  # Defaults to `right`.
    pose: MannequinPose | None = None  # Defaults to `standing`.
    immovable: bool | None = None  # Defaults to `false`.
    description: Text | None = None  # Text shown below the name tag. Defaults to the translated `entity.minecraft.mannequin.label`.
    hide_description: bool | None = None  # Whether the below name text is displayed. Defaults to `false`.
    equipment: EntityEquipment | None = None  # The equipment items of the mannequin.


@dataclass(kw_only=True)
class EnderPearlMarker(EntityBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:marker']  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlMinecart(EntityBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:minecart']  # The ID of this entity. Not present on player entities.
    DisplayState: BlockState2 | None = None  # Custom block to display.
    DisplayOffset: int | None = None  # Vertical offset of the block display.


@dataclass(kw_only=True)
class EnderPearlMooshroom(Breedable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:mooshroom']  # The ID of this entity. Not present on player entities.
    Type: MooshroomType | None = None
    stew_effects: list[SuspiciousStewEffect] | None = None


@dataclass(kw_only=True)
class EnderPearlMule(HorseBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:mule']  # The ID of this entity. Not present on player entities.
    ChestedHorse: bool | None = None  # Whether it has a chest.
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`14` | both inclusive']] | ItemsStruct], 'Length = 0-15 (both inclusive)'] | None = None  # Slots from 0 to 14.


@dataclass(kw_only=True)
class EnderPearlNautilus(Breedable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:nautilus']  # The ID of this entity. Not present on player entities.
    Owner: tuple[int, int, int, int] | None = None
    Sitting: bool | None = None  # Whether the mob is sitting.


@dataclass(kw_only=True)
class EnderPearlOakBoat(EntityBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:oak_boat']  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlOakChestBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:oak_chest_boat']  # The ID of this entity. Not present on player entities.
    LootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that will populate this chest boat.
    LootTableSeed: int | None = None  # Seed of the loot table.
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`26` | both inclusive']]], 'Length = 0-27 (both inclusive)'] | None = None  # Slots from 0 to 26.


@dataclass(kw_only=True)
class EnderPearlOcelot(Breedable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:ocelot']  # The ID of this entity. Not present on player entities.
    Trusting: bool | None = None  # Whether it trusts players.


@dataclass(kw_only=True)
class EnderPearlOminousItemSpawner(EntityBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:ominous_item_spawner']  # The ID of this entity. Not present on player entities.
    item: ItemStack | None = None
    spawn_item_after_ticks: int | None = None


@dataclass(kw_only=True)
class EnderPearlPainting(BlockAttachedEntity):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:painting']  # The ID of this entity. Not present on player entities.
    facing: HorizontalDirectionByte | None = None  # Direction it is facing.
    variant: Annotated[str, IdSpec(registry='painting_variant')] | None = None  # Type of painting.


@dataclass(kw_only=True)
class EnderPearlPaleOakBoat(EntityBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:pale_oak_boat']  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlPaleOakChestBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:pale_oak_chest_boat']  # The ID of this entity. Not present on player entities.
    LootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that will populate this chest boat.
    LootTableSeed: int | None = None  # Seed of the loot table.
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`26` | both inclusive']]], 'Length = 0-27 (both inclusive)'] | None = None  # Slots from 0 to 26.


@dataclass(kw_only=True)
class EnderPearlPanda(Breedable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:panda']  # The ID of this entity. Not present on player entities.
    MainGene: Gene | None = None  # Displayed gene. If this gene is recessive and 'HiddenGene' is not the same, the panda will display the 'normal' gene.
    HiddenGene: Gene | None = None  # Hidden gene.


@dataclass(kw_only=True)
class EnderPearlParched(LivingEntity):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:parched']  # The ID of this entity. Not present on player entities.
    equipment: EntityEquipment | None = None  # The equipment items of the mob, such as armor or weapons.
    drop_chances: DropChances | None = None  # Chances of the mob dropping an equipment slot on death.
    DeathLootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that is dropped when the mob dies.
    DeathLootTableSeed: int | None = None  # Seed for generating the death loot table.
    CanPickUpLoot: bool | None = None  # Whether it can pick up loot.
    PersistenceRequired: bool | None = None  # Whether it should not despawn naturally.
    LeftHanded: bool | None = None  # Whether it is left handed.
    NoAI: bool | None = None  # Whether it should have an AI.
    leash: tuple[int, int, int] | LeashStruct | None = None  # What the leash is attached to.
    home_radius: int | None = None  # Defaults to -1, which represents "no home".
    home_pos: tuple[int, int, int] | None = None  # This field will be discarded if `home_radius` is less than 0.


@dataclass(kw_only=True)
class EnderPearlParrot(Tamable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:parrot']  # The ID of this entity. Not present on player entities.
    Variant: ParrotVariantInt | None = None


@dataclass(kw_only=True)
class EnderPearlPhantom(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:phantom']  # The ID of this entity. Not present on player entities.
    anchor_pos: tuple[int, int, int] | None = None  # Approximate circle coordinates.
    size: Annotated[int, 'Range | `0`-`64` | both inclusive'] | None = None


@dataclass(kw_only=True)
class EnderPearlPig(Saddled):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:pig']  # The ID of this entity. Not present on player entities.
    variant: Annotated[str, IdSpec(registry='pig_variant')] | None = None
    sound_variant: Annotated[str, IdSpec(registry='pig_sound_variant')] | None = None


@dataclass(kw_only=True)
class EnderPearlPiglin(PiglinBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:piglin']  # The ID of this entity. Not present on player entities.
    IsBaby: bool | None = None  # Whether it is a baby.
    CannotHunt: bool | None = None  # Whether it does not hunt hoglins.
    Inventory: Annotated[list[ItemStack], 'Length = 0-8 (both inclusive)'] | None = None


@dataclass(kw_only=True)
class EnderPearlPiglinBrute(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:piglin_brute']  # The ID of this entity. Not present on player entities.
    IsImmuneToZombification: bool | None = None  # Whether it will not transform to a zombified piglin when it is in the Overworld.
    TimeInOverworld: int | None = None  # Ticks it has been in the overworld.


@dataclass(kw_only=True)
class EnderPearlPillager(RaiderBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:pillager']  # The ID of this entity. Not present on player entities.
    Inventory: Annotated[list[ItemStack], 'Length = 0-5 (both inclusive)'] | None = None


@dataclass(kw_only=True)
class EnderPearlPlayer(LivingEntity):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:player']  # The ID of this entity. Not present on player entities.
    DataVersion: int | None = None  # Version of the player NBT structure
    Dimension: Annotated[str, IdSpec(registry='dimension')] | None = None
    LastDeathLocation: GlobalPos | None = None  # Location of the player's last death.
    playerGameType: Gamemode | None = None  # Game mode that the player is in.
    previousPlayerGameType: Gamemode | None = None  # Previous game mode that the player was in.
    Score: int | None = None  # Score to display upon death.
    SelectedItemSlot: Annotated[int, 'Range | `0`-`8` | both inclusive'] | None = None  # Hotbar slot the player has selected.
    SelectedItem: SlottedItem[Annotated[int, 'Range | `0`-`8` | both inclusive']] | None = None  # Item in the hotbar slot the player has selected.
    equipment: PlayerEquipment | None = None
    respawn: Respawn | None = None
    SleepTimer: int | None = None  # Ticks the player has been in bed.
    foodLevel: int | None = None  # Level of the hunger bar.
    foodExhaustionLevel: float | None = None  # Rate at which the `foodSaturationLevel` depletes.
    foodSaturationLevel: float | None = None  # Rate at which the hunger bar depletes.
    foodTickTimer: int | None = None  # Ticks until the player heals or takes starvation damage.
    XpLevel: int | None = None  # Number of experience levels the player has.
    XpP: float | None = None  # Percentage the experience bar is filled up.
    XpTotal: int | None = None  # Total experience the player has.
    XpSeed: int | None = None  # Seed for enchantments.
    Inventory: Annotated[list[SlottedItem[PlayerSlot]], 'Length = 0-41 (both inclusive)'] | None = None
    EnderItems: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`26` | both inclusive']]], 'Length = 0-27 (both inclusive)'] | None = None  # The player's enderchest inventory.
    abilities: Abilities | None = None  # Abilities of the player.
    entered_nether_pos: tuple[float, float, float] | None = None  # Position that the player entered the nether at.
    raid_omen_position: tuple[int, int, int] | None = None
    RootVehicle: RootVehicle | None = None  # Entity that the player is riding.
    ShoulderEntityLeft: AnyEntity | None = None  # Entity that is on the player's left shoulder.
    ShoulderEntityRight: AnyEntity | None = None  # Entity that is on the player's right shoulder.
    seenCredits: bool | None = None  # Whether the player has gone to the overworld after defeating the Ender Dragon.
    recipeBook: RecipeBook | None = None  # Recipes that the player has.
    warden_spawn_tracker: WardenSpawnTracker | None = None  # Tracking the warden spawning process for this player.
    ender_pearls: list[EnderPearl] | None = None  # Ender pearls thrown by this player.
    post_effects: list[Annotated[str, IdSpec(registry='post_effect')]] | None = None
    last_explosion_impact_pos: tuple[float, float, float] | None = None
    spawn_extra_particles_on_fall: bool | None = None


@dataclass(kw_only=True)
class EnderPearlPolarBear(Breedable, NeutralMob):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:polar_bear']  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlPoplarBoat(EntityBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:poplar_boat']  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlPopolarChestBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:popolar_chest_boat']  # The ID of this entity. Not present on player entities.
    LootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that will populate this chest boat.
    LootTableSeed: int | None = None  # Seed of the loot table.
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`26` | both inclusive']]], 'Length = 0-27 (both inclusive)'] | None = None  # Slots from 0 to 26.


@dataclass(kw_only=True)
class EnderPearlPotion(Throwable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:potion']  # The ID of this entity. Not present on player entities.
    Item: ItemStack | None = None  # Item representation of the potion.


@dataclass(kw_only=True)
class EnderPearlPufferfish(Fish):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:pufferfish']  # The ID of this entity. Not present on player entities.
    PuffState: PuffState | None = None  # How puffed it is.


@dataclass(kw_only=True)
class EnderPearlRabbit(Breedable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:rabbit']  # The ID of this entity. Not present on player entities.
    RabbitType: RabbitType | None = None
    MoreCarrotTicks: int | None = None  # Ticks down once a carrot crop is eaten


@dataclass(kw_only=True)
class EnderPearlRavager(RaiderBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:ravager']  # The ID of this entity. Not present on player entities.
    AttackTick: int | None = None  # Ticks until it can attack.
    RoarTick: int | None = None  # Ticks until it can roar.
    StunTick: int | None = None  # Ticks it is stunned for.


@dataclass(kw_only=True)
class EnderPearlSalmon(Fish):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:salmon']  # The ID of this entity. Not present on player entities.
    type: SalmonType | None = None  # The size variant of the salmon.


@dataclass(kw_only=True)
class EnderPearlSheep(Breedable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:sheep']  # The ID of this entity. Not present on player entities.
    Sheared: bool | None = None  # Whether it has been shorn.
    Color: DyeColorByte | None = None


@dataclass(kw_only=True)
class EnderPearlShulker(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:shulker']  # The ID of this entity. Not present on player entities.
    Peek: bool | None = None  # Whether it is peeking.
    AttachFace: DirectionByte | None = None  # Which face it is attached to.
    Color: DyeColorByte2 | ShulkerColor | None = None


@dataclass(kw_only=True)
class EnderPearlShulkerBullet(ProjectileBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:shulker_bullet']  # The ID of this entity. Not present on player entities.
    Steps: int | None = None  # Steps it takes to reach the target
    Target: BulletTarget | None = None
    Dir: DirectionByte | None = None
    TXD: float | None = None  # X offset to move based on the target's location.
    TYD: float | None = None  # Y offset to move based on the target's location.
    TZD: float | None = None  # Z offset to move based on the target's location.


@dataclass(kw_only=True)
class EnderPearlSilverfish(LivingEntity):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:silverfish']  # The ID of this entity. Not present on player entities.
    equipment: EntityEquipment | None = None  # The equipment items of the mob, such as armor or weapons.
    drop_chances: DropChances | None = None  # Chances of the mob dropping an equipment slot on death.
    DeathLootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that is dropped when the mob dies.
    DeathLootTableSeed: int | None = None  # Seed for generating the death loot table.
    CanPickUpLoot: bool | None = None  # Whether it can pick up loot.
    PersistenceRequired: bool | None = None  # Whether it should not despawn naturally.
    LeftHanded: bool | None = None  # Whether it is left handed.
    NoAI: bool | None = None  # Whether it should have an AI.
    leash: tuple[int, int, int] | LeashStruct | None = None  # What the leash is attached to.
    home_radius: int | None = None  # Defaults to -1, which represents "no home".
    home_pos: tuple[int, int, int] | None = None  # This field will be discarded if `home_radius` is less than 0.


@dataclass(kw_only=True)
class EnderPearlSkeleton(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:skeleton']  # The ID of this entity. Not present on player entities.
    StrayConversionTime: int | None = None  # Time until it converts to a stray.


@dataclass(kw_only=True)
class EnderPearlSkeletonHorse(HorseBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:skeleton_horse']  # The ID of this entity. Not present on player entities.
    SkeletonTrap: bool | None = None  # Whether it was spawned by a trap.
    SkeletonTrapTime: int | None = None  # Ticks it has existed.


@dataclass(kw_only=True)
class EnderPearlSlime(CubeMob, MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:slime']  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlSmallFireball(DespawnableProjectileBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:small_fireball']  # The ID of this entity. Not present on player entities.
    Item: ItemStack | None = None  # Item it should render as.


@dataclass(kw_only=True)
class EnderPearlSniffer(AgeableMob, MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:sniffer']  # The ID of this entity. Not present on player entities.
    InLove: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # Ticks until it stops searching for a mate.
    LoveCause: tuple[int, int, int, int] | None = None  # Player that caused this mob to breed.


@dataclass(kw_only=True)
class EnderPearlSnowGolem(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:snow_golem']  # The ID of this entity. Not present on player entities.
    Pumpkin: bool | None = None  # Whether it has a pumpkin.


@dataclass(kw_only=True)
class EnderPearlSnowball(Throwable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:snowball']  # The ID of this entity. Not present on player entities.
    Item: ItemStack | None = None  # Item representation of the projectile.


@dataclass(kw_only=True)
class EnderPearlSpawnerMinecart(Minecart):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:spawner_minecart']  # The ID of this entity. Not present on player entities.
    SpawnPotentials: list[SpawnPotential] | None = None  # List of potential entities to place next.
    SpawnData: SpawnerEntry | None = None  # Data for the next mob to place. Will be overwritten by `SpawnPotentials`.
    SpawnCount: int  # Number of entities that will be placed.
    SpawnRange: int | None = None  # Range that the spawned entities will be placed in.
    Delay: int | None = None  # Ticks until the next spawn.
    MinSpawnDelay: int | None = None  # Minimum random delay for the next spawn.
    MaxSpawnDelay: int | None = None  # Maximum random delay for the next spawn.
    MaxNearbyEntities: int | None = None  # Maximum number of entities nearby.
    RequiredPlayerRange: int | None = None  # Radius in blocks that a player has to be within to spawn entities.


@dataclass(kw_only=True)
class EnderPearlSpectralArrow(ArrowBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:spectral_arrow']  # The ID of this entity. Not present on player entities.
    Duration: int | None = None  # Ticks the glowing effect lasts.


@dataclass(kw_only=True)
class EnderPearlSpider(LivingEntity):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:spider']  # The ID of this entity. Not present on player entities.
    equipment: EntityEquipment | None = None  # The equipment items of the mob, such as armor or weapons.
    drop_chances: DropChances | None = None  # Chances of the mob dropping an equipment slot on death.
    DeathLootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that is dropped when the mob dies.
    DeathLootTableSeed: int | None = None  # Seed for generating the death loot table.
    CanPickUpLoot: bool | None = None  # Whether it can pick up loot.
    PersistenceRequired: bool | None = None  # Whether it should not despawn naturally.
    LeftHanded: bool | None = None  # Whether it is left handed.
    NoAI: bool | None = None  # Whether it should have an AI.
    leash: tuple[int, int, int] | LeashStruct | None = None  # What the leash is attached to.
    home_radius: int | None = None  # Defaults to -1, which represents "no home".
    home_pos: tuple[int, int, int] | None = None  # This field will be discarded if `home_radius` is less than 0.


@dataclass(kw_only=True)
class EnderPearlSplashPotion(Throwable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:splash_potion']  # The ID of this entity. Not present on player entities.
    Item: ItemStack | None = None  # Item representation of the potion.


@dataclass(kw_only=True)
class EnderPearlSpruceBoat(EntityBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:spruce_boat']  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlSpruceChestBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:spruce_chest_boat']  # The ID of this entity. Not present on player entities.
    LootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that will populate this chest boat.
    LootTableSeed: int | None = None  # Seed of the loot table.
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`26` | both inclusive']]], 'Length = 0-27 (both inclusive)'] | None = None  # Slots from 0 to 26.


@dataclass(kw_only=True)
class EnderPearlSquid(AgeableMob, MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:squid']  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlStray(LivingEntity):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:stray']  # The ID of this entity. Not present on player entities.
    equipment: EntityEquipment | None = None  # The equipment items of the mob, such as armor or weapons.
    drop_chances: DropChances | None = None  # Chances of the mob dropping an equipment slot on death.
    DeathLootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that is dropped when the mob dies.
    DeathLootTableSeed: int | None = None  # Seed for generating the death loot table.
    CanPickUpLoot: bool | None = None  # Whether it can pick up loot.
    PersistenceRequired: bool | None = None  # Whether it should not despawn naturally.
    LeftHanded: bool | None = None  # Whether it is left handed.
    NoAI: bool | None = None  # Whether it should have an AI.
    leash: tuple[int, int, int] | LeashStruct | None = None  # What the leash is attached to.
    home_radius: int | None = None  # Defaults to -1, which represents "no home".
    home_pos: tuple[int, int, int] | None = None  # This field will be discarded if `home_radius` is less than 0.


@dataclass(kw_only=True)
class EnderPearlStrider(Breedable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:strider']  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlSulfurCube(AgeableMob, CubeMob, MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:sulfur_cube']  # The ID of this entity. Not present on player entities.
    pickup_timer: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None
    from_bucket: bool | None = None
    fuse: Annotated[int, 'Range | Min `-1` and above | inclusive'] | None = None  # `-1` represents "not ignited".


@dataclass(kw_only=True)
class EnderPearlTadpole(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:tadpole']  # The ID of this entity. Not present on player entities.
    Age: int | None = None  # Age of it in ticks. When greater than or equal to 24000, it grows into a frog.
    FromBucket: bool | None = None  # If it was released from a bucket.


@dataclass(kw_only=True)
class EnderPearlTextDisplay(DisplayBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:text_display']  # The ID of this entity. Not present on player entities.
    text: Text | None = None  # Text to display. Components are resolved with the executor set to the display entity and the position set to `0 0 0`.
    line_width: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # Line width in pixels used to split lines (note: new line can also be added with `\n` characters). Defaults to 200.
    text_opacity: Annotated[int, 'Range | `0`-`255` | both inclusive'] | None = None  # Opacity (alpha component) of rendered text. Defaults to 255. Interpolated.
    background: int | None = None  # Color of background. Includes alpha channel. Defaults to 0x40000000. Interpolated.  Calculated as `ALPHA << 24 | RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.
    default_background: bool | None = None  # If true, overrides `background` & rendering uses default text background color (same as in chat). Defaults to false.
    shadow: bool | None = None  # Whether to display the text with shadows. Defaults to false.
    see_through: bool | None = None  # Whether the text should be visible through opaque blocks. Defaults to false.
    alignment: TextAlignment | None = None  # How text should be aligned. Defaults to `center`.


@dataclass(kw_only=True)
class EnderPearlTnt(EntityBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:tnt']  # The ID of this entity. Not present on player entities.
    fuse: int | None = None  # Ticks until it explodes.
    block_state: BlockState | None = None  # Defaults to tnt.
    explosion_power: Annotated[float, 'Range | `0`-`128` | both inclusive'] | None = None
    owner: tuple[int, int, int, int] | None = None  # The entity that primed this TNT.


@dataclass(kw_only=True)
class EnderPearlTntMinecart(Minecart):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:tnt_minecart']  # The ID of this entity. Not present on player entities.
    fuse: int | None = None  # Ticks until it explodes.
    explosion_power: Annotated[float, 'Range | `0`-`128` | both inclusive'] | None = None
    explosion_speed_factor: Annotated[float, 'Range | `0`-`128` | both inclusive'] | None = None  # Controls the amount of added damage depending on the speed of the minecart.


@dataclass(kw_only=True)
class EnderPearlTraderLlama(Llama):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:trader_llama']  # The ID of this entity. Not present on player entities.
    DespawnDelay: int | None = None  # When it will despawn.


@dataclass(kw_only=True)
class EnderPearlTrident(ArrowBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:trident']  # The ID of this entity. Not present on player entities.
    DealtDamage: bool | None = None  # Whether it has already damaged an entity.


@dataclass(kw_only=True)
class EnderPearlTropicalFish(Fish):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:tropical_fish']  # The ID of this entity. Not present on player entities.
    Variant: int | None = None


@dataclass(kw_only=True)
class EnderPearlTurtle(Breedable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:turtle']  # The ID of this entity. Not present on player entities.
    has_egg: bool | None = None  # Whether it has an egg.
    home_pos: tuple[int, int, int] | None = None


@dataclass(kw_only=True)
class EnderPearlVex(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:vex']  # The ID of this entity. Not present on player entities.
    bound_pos: tuple[int, int, int] | None = None  # Coordinates of the center of its wander bounds.
    life_ticks: int | None = None  # Ticks until it starts to die.
    owner: tuple[int, int, int, int] | None = None  # The owner of this vex.


@dataclass(kw_only=True)
class EnderPearlVillager(Breedable, VillagerBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:villager']  # The ID of this entity. Not present on player entities.
    VillagerData: VillagerData | None = None
    VillagerDataFinalized: bool | None = None
    FoodLevel: Annotated[int, 'Range | `0`-`12` | both inclusive'] | None = None  # Determines whether the villager will be available to reproduce.  When the value is `12` the villager can reproduce.  After reproducing, the value is reset to `0`.  To increase this value villagers will pick up food that is in range.  Foods: Potatoes, Carrots, & Beetroots increase the level by `1`. Bread increases the level by `4`.
    Gossips: list[PlayerReputationPart] | None = None  # Affects per-player reputation which affects trade offer pricing and iron golem behavior.  Reputation is assembled through events the villager has witnessed (within 16 blocks) or heard about from other villagers through gossip.  All reputation parts decay over time except `major_positive` which is only ever increased (when the villager is cured).  Decay occurs every 24k ticks (20 minutes), tracked by `LastGossipDecay`.  Once a reputation part decays to zero it is removed from the list.
    LastGossipDecay: int | None = None  # Last game-tick every gossip significance `Value` could have decayed.  Once this reaches 24k (20 minutes) less than the current game tick a decay occurs again.
    LastRestock: int | None = None  # Last game-tick it removed `uses` & updated `demand` of every trade offer by going to its `job_site`.
    RestocksToday: Annotated[int, 'Range | `0`-`2` | both inclusive'] | None = None  # Times it has reset the `uses` & updated `demand` of every trade offer by going to its `job_site` in the past 12k ticks (10 minutes).  Time is tracked by `LastRestock`.  When two restocks have occurred, another restock (and reset of this value to `0`) will only occur after 10 minutes.
    Xp: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # XP it has, increases when trades are used by each trade offer's `xp` value.  After `250` the XP will continue to increase, but will do nothing more.  Trade tiers: - `0..9`     - Tier 1: Novice - `10..69`   - Tier 2: Apprentice - `70..149`  - Tier 3: Journeyman - `150..249` - Tier 4: Expert - `250..`    - Tier 5: Master


@dataclass(kw_only=True)
class EnderPearlVindicator(RaiderBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:vindicator']  # The ID of this entity. Not present on player entities.
    Johnny: bool | None = None  # Whether it should try to attack most other mobs.


@dataclass(kw_only=True)
class EnderPearlWanderingTrader(MobBase, VillagerBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:wandering_trader']  # The ID of this entity. Not present on player entities.
    DespawnDelay: int | None = None  # Ticks until it despawns.
    wander_target: tuple[int, int, int] | None = None  # Where it is heading to.


@dataclass(kw_only=True)
class EnderPearlWarden(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:warden']  # The ID of this entity. Not present on player entities.
    anger: AngerManagement | None = None  # Anger management
    listener: VibrationListener | None = None  # Vibration listener


@dataclass(kw_only=True)
class EnderPearlWitch(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:witch']  # The ID of this entity. Not present on player entities.
    Patrolling: bool | None = None  # Whether the raider is patrolling.
    PatrolLeader: bool | None = None  # Whether the raider is leading the patrol.
    patrol_target: tuple[int, int, int] | None = None  # Where the raider is heading towards.
    CanJoinRaid: bool | None = None  # Whether the raider can join raids and count towards the progress bar.
    RaidId: int | None = None  # Id of the raid that the raider is in.
    Wave: Annotated[int, 'Range | `0`-`8` | both inclusive'] | None = None  # Wave that the raider is in.


@dataclass(kw_only=True)
class EnderPearlWither(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:wither']  # The ID of this entity. Not present on player entities.
    Invul: int | None = None  # Ticks it is invulnerable for.


@dataclass(kw_only=True)
class EnderPearlWitherSkeleton(LivingEntity):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:wither_skeleton']  # The ID of this entity. Not present on player entities.
    equipment: EntityEquipment | None = None  # The equipment items of the mob, such as armor or weapons.
    drop_chances: DropChances | None = None  # Chances of the mob dropping an equipment slot on death.
    DeathLootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that is dropped when the mob dies.
    DeathLootTableSeed: int | None = None  # Seed for generating the death loot table.
    CanPickUpLoot: bool | None = None  # Whether it can pick up loot.
    PersistenceRequired: bool | None = None  # Whether it should not despawn naturally.
    LeftHanded: bool | None = None  # Whether it is left handed.
    NoAI: bool | None = None  # Whether it should have an AI.
    leash: tuple[int, int, int] | LeashStruct | None = None  # What the leash is attached to.
    home_radius: int | None = None  # Defaults to -1, which represents "no home".
    home_pos: tuple[int, int, int] | None = None  # This field will be discarded if `home_radius` is less than 0.


@dataclass(kw_only=True)
class EnderPearlWitherSkull(DespawnableProjectileBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:wither_skull']  # The ID of this entity. Not present on player entities.
    dangerous: bool | None = None


@dataclass(kw_only=True)
class EnderPearlWolf(NeutralMob, Tamable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:wolf']  # The ID of this entity. Not present on player entities.
    CollarColor: DyeColorByte | None = None  # Collar color, present for wild wolfs. Defaults to 14 (red).
    variant: Annotated[str, IdSpec(registry='wolf_variant')] | None = None
    sound_variant: Annotated[str, IdSpec(registry='wolf_sound_variant')] | None = None


@dataclass(kw_only=True)
class EnderPearlZoglin(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:zoglin']  # The ID of this entity. Not present on player entities.
    IsBaby: bool | None = None  # Whether it is a baby.


@dataclass(kw_only=True)
class EnderPearlZombie(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:zombie']  # The ID of this entity. Not present on player entities.
    IsBaby: bool | None = None  # Whether it is a baby.
    CanBreakDoors: bool | None = None  # Whether it can break doors.
    DrownedConversionTime: int | None = None  # Ticks until it converts.
    InWaterTime: int | None = None  # Ticks it has been in the water.


@dataclass(kw_only=True)
class EnderPearlZombieHorse(Breedable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:zombie_horse']  # The ID of this entity. Not present on player entities.
    Bred: bool | None = None  # Unknown use. Remains `0` even if it was bred.
    EatingHaystack: bool | None = None  # Whether it is eating a haystack.
    Tame: bool | None = None  # Whether it has been tamed.
    Temper: Annotated[int, 'Range | `0`-`100` | both inclusive'] | None = None  # Higher values make it easier to tame. Increases with feeding.
    Owner: tuple[int, int, int, int] | None = None  # Player who tamed it.


@dataclass(kw_only=True)
class EnderPearlZombieNautilus(Breedable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:zombie_nautilus']  # The ID of this entity. Not present on player entities.
    Owner: tuple[int, int, int, int] | None = None
    Sitting: bool | None = None  # Whether the mob is sitting.


@dataclass(kw_only=True)
class EnderPearlZombiePigman(MobBase, NeutralMob):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:zombie_pigman']  # The ID of this entity. Not present on player entities.
    IsBaby: bool | None = None  # Whether it is a baby.
    HurtBy: str | None = None  # Last player to hit a zombie pigman in this zombie pigman's detection range.


@dataclass(kw_only=True)
class EnderPearlZombieVillager(Zombie):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:zombie_villager']  # The ID of this entity. Not present on player entities.
    VillagerData: VillagerData | None = None  # Villager's skin data
    VillagerDataFinalized: bool | None = None
    Gossips: list[PlayerReputationPart] | None = None  # Villager's gossips
    Offers: Offers | None = None  # Villager's offers
    ConversionTime: int | None = None  # Ticks until the it is converted.
    ConversionPlayer: tuple[int, int, int, int] | None = None  # Player who triggered the conversion.


@dataclass(kw_only=True)
class EnderPearlZombifiedPiglin(MobBase, NeutralMob):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:zombified_piglin']  # The ID of this entity. Not present on player entities.
    IsBaby: bool | None = None  # Whether it is a baby.
    HurtBy: str | None = None  # Last player to hit a zombie pigman in this zombie pigman's detection range.


type EnderPearl = EnderPearlAcaciaBoat | EnderPearlAcaciaChestBoat | EnderPearlAllay | EnderPearlAreaEffectCloud | EnderPearlArmadillo | EnderPearlArmorStand | EnderPearlArrow | EnderPearlAxolotl | EnderPearlBambooChestRaft | EnderPearlBambooRaft | EnderPearlBat | EnderPearlBee | EnderPearlBirchBoat | EnderPearlBirchChestBoat | EnderPearlBlaze | EnderPearlBlockDisplay | EnderPearlBoat | EnderPearlBogged | EnderPearlBreeze | EnderPearlBreezeWindCharge | EnderPearlCamel | EnderPearlCamelHusk | EnderPearlCat | EnderPearlCaveSpider | EnderPearlCherryBoat | EnderPearlCherryChestBoat | EnderPearlChestBoat | EnderPearlChestMinecart | EnderPearlChicken | EnderPearlCod | EnderPearlCommandBlockMinecart | EnderPearlCopperGolem | EnderPearlCow | EnderPearlCreaking | EnderPearlCreakingTransient | EnderPearlCreeper | EnderPearlCushion | EnderPearlDarkOakBoat | EnderPearlDarkOakChestBoat | EnderPearlDolphin | EnderPearlDonkey | EnderPearlDragonFireball | EnderPearlDrowned | EnderPearlEgg | EnderPearlElderGuardian | EnderPearlEndCrystal | EnderPearlEnderDragon | EnderPearlEnderPearl | EnderPearlEnderman | EnderPearlEndermite | EnderPearlEvoker | EnderPearlEvokerFangs | EnderPearlExperienceBottle | EnderPearlExperienceOrb | EnderPearlEyeOfEnder | EnderPearlFallingBlock | EnderPearlFireball | EnderPearlFireworkRocket | EnderPearlFox | EnderPearlFrog | EnderPearlFurnaceMinecart | EnderPearlGhast | EnderPearlGiant | EnderPearlGlowItemFrame | EnderPearlGlowSquid | EnderPearlGoat | EnderPearlGuardian | EnderPearlHappyGhast | EnderPearlHoglin | EnderPearlHopperMinecart | EnderPearlHorse | EnderPearlHusk | EnderPearlIllusioner | EnderPearlInteraction | EnderPearlIronGolem | EnderPearlItem | EnderPearlItemDisplay | EnderPearlItemFrame | EnderPearlJungleBoat | EnderPearlJungleChestBoat | EnderPearlLeashKnot | EnderPearlLingeringPotion | EnderPearlLlama | EnderPearlLlamaSpit | EnderPearlMagmaCube | EnderPearlMangroveBoat | EnderPearlMangroveChestBoat | EnderPearlMannequin | EnderPearlMarker | EnderPearlMinecart | EnderPearlMooshroom | EnderPearlMule | EnderPearlNautilus | EnderPearlOakBoat | EnderPearlOakChestBoat | EnderPearlOcelot | EnderPearlOminousItemSpawner | EnderPearlPainting | EnderPearlPaleOakBoat | EnderPearlPaleOakChestBoat | EnderPearlPanda | EnderPearlParched | EnderPearlParrot | EnderPearlPhantom | EnderPearlPig | EnderPearlPiglin | EnderPearlPiglinBrute | EnderPearlPillager | EnderPearlPlayer | EnderPearlPolarBear | EnderPearlPoplarBoat | EnderPearlPopolarChestBoat | EnderPearlPotion | EnderPearlPufferfish | EnderPearlRabbit | EnderPearlRavager | EnderPearlSalmon | EnderPearlSheep | EnderPearlShulker | EnderPearlShulkerBullet | EnderPearlSilverfish | EnderPearlSkeleton | EnderPearlSkeletonHorse | EnderPearlSlime | EnderPearlSmallFireball | EnderPearlSniffer | EnderPearlSnowGolem | EnderPearlSnowball | EnderPearlSpawnerMinecart | EnderPearlSpectralArrow | EnderPearlSpider | EnderPearlSplashPotion | EnderPearlSpruceBoat | EnderPearlSpruceChestBoat | EnderPearlSquid | EnderPearlStray | EnderPearlStrider | EnderPearlSulfurCube | EnderPearlTadpole | EnderPearlTextDisplay | EnderPearlTnt | EnderPearlTntMinecart | EnderPearlTraderLlama | EnderPearlTrident | EnderPearlTropicalFish | EnderPearlTurtle | EnderPearlVex | EnderPearlVillager | EnderPearlVindicator | EnderPearlWanderingTrader | EnderPearlWarden | EnderPearlWitch | EnderPearlWither | EnderPearlWitherSkeleton | EnderPearlWitherSkull | EnderPearlWolf | EnderPearlZoglin | EnderPearlZombie | EnderPearlZombieHorse | EnderPearlZombieNautilus | EnderPearlZombiePigman | EnderPearlZombieVillager | EnderPearlZombifiedPiglin


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::player::EnderPearl": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "ender_pearl_dimension",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "dimension"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::AnyEntity"
                }
            }
        ]
    }
}

