"""
Generated from symbols.json for ::java::world::entity::mob::player::Player
Local link to file: vanilla_mcdoc/world/entity/mob/player/Player.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.world.entity.mob.LivingEntity import LivingEntity

if TYPE_CHECKING:
    from vanilla_mcdoc.util.GlobalPos import GlobalPos
    from vanilla_mcdoc.util.slot.SlottedItem import SlottedItem
    from vanilla_mcdoc.world.entity.AnyEntity import AnyEntity
    from vanilla_mcdoc.world.entity.mob.player.Abilities import Abilities
    from vanilla_mcdoc.world.entity.mob.player.EnderPearl import EnderPearl
    from vanilla_mcdoc.world.entity.mob.player.Gamemode import Gamemode
    from vanilla_mcdoc.world.entity.mob.player.PlayerEquipment import PlayerEquipment
    from vanilla_mcdoc.world.entity.mob.player.PlayerSlot import PlayerSlot
    from vanilla_mcdoc.world.entity.mob.player.RecipeBook import RecipeBook
    from vanilla_mcdoc.world.entity.mob.player.Respawn import Respawn
    from vanilla_mcdoc.world.entity.mob.player.RootVehicle import RootVehicle
    from vanilla_mcdoc.world.entity.mob.player.WardenSpawnTracker import WardenSpawnTracker


class Player(LivingEntity):
    DataVersion: int | None = None  # Version of the player NBT structure
    Dimension: Annotated[str, IdSpec(registry='dimension')] | None = None
    LastDeathLocation: GlobalPos | None = None  # Location of the player's last death.
    playerGameType: Gamemode | None = None  # Game mode that the player is in.
    previousPlayerGameType: Gamemode | None = None  # Previous game mode that the player was in.
    Score: int | None = None  # Score to display upon death.
    SelectedItemSlot: Annotated[int, Field(ge=0, le=8)] | None = None  # Hotbar slot the player has selected.
    SelectedItem: SlottedItem[Annotated[int, Field(ge=0, le=8)]] | None = None  # Item in the hotbar slot the player has selected.
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
    Inventory: Annotated[list[SlottedItem[PlayerSlot]], Field(min_length=0, max_length=41)] | None = None
    EnderItems: Annotated[list[SlottedItem[Annotated[int, Field(ge=0, le=26)]]], Field(min_length=0, max_length=27)] | None = None  # The player's enderchest inventory.
    abilities: Abilities | None = None  # Abilities of the player.
    entered_nether_pos: tuple[float, float, float] | None = None  # Position that the player entered the nether at.
    raid_omen_position: tuple[int, int, int] | None = None
    RootVehicle_: RootVehicle | None = Field(default=None, alias='RootVehicle')  # Entity that the player is riding.
    ShoulderEntityLeft: AnyEntity | None = None  # Entity that is on the player's left shoulder.
    ShoulderEntityRight: AnyEntity | None = None  # Entity that is on the player's right shoulder.
    seenCredits: bool | None = None  # Whether the player has gone to the overworld after defeating the Ender Dragon.
    recipeBook: RecipeBook | None = None  # Recipes that the player has.
    warden_spawn_tracker: WardenSpawnTracker | None = None  # Tracking the warden spawning process for this player.
    ender_pearls: list[EnderPearl] | None = None  # Ender pearls thrown by this player.
    post_effects: list[Annotated[str, IdSpec(registry='post_effect')]] | None = None
    last_explosion_impact_pos: tuple[float, float, float] | None = None
    spawn_extra_particles_on_fall: bool | None = None
