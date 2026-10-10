"""
Generated from symbols.json for ::java::world::entity::mob::LivingEntity
Local link to file: vanilla_mcdoc/world/entity/mob/LivingEntity.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import MinecraftUUID
from vanilla_mcdoc.world.entity.EntityBase import EntityBase
from vanilla_mcdoc.world.entity.mob.FallDamageLogicData import FallDamageLogicData

if TYPE_CHECKING:
    from vanilla_mcdoc.util.effect.MobEffectInstance import MobEffectInstance
    from vanilla_mcdoc.util.memory.Memories import Memories
    from vanilla_mcdoc.world.entity.mob.Attribute import Attribute
    from vanilla_mcdoc.world.entity.mob.WaypointIcon import WaypointIcon


class BrainStruct(GeneratedModel):
    memories: Memories | None = None


class LivingEntity(EntityBase, FallDamageLogicData):
    Health: float | None = None
    AbsorptionAmount: float | None = None  # How much absorption health it has.
    HurtTime: int | None = None  # Timer since it has been damaged. Counts down to zero.
    DeathTime: int | None = None  # Timer since it was marked as dead. Counts down to zero.
    FallFlying: bool | None = None  # Whether it will glide when it falls.
    sleeping_pos: tuple[int, int, int] | None = None
    Brain: BrainStruct | None = None
    attributes: list[Attribute] | None = None
    active_effects: list[MobEffectInstance] | None = None
    last_hurt_by_player: MinecraftUUID | None = None  # The UUID of the player that last hurt this entity. Stored for 100 ticks.
    last_hurt_by_player_memory_time: Annotated[int, Field(ge=0, le=100)] | None = None  # Amount of ticks that this entity will remember the player that last hurt this entity. Counts down from 100 to 0.
    last_hurt_by_mob: MinecraftUUID | None = None  # The UUID of the mob that last hurt this entity. Stored for 100 ticks.
    ticks_since_last_hurt_by_mob: Annotated[int, Field(ge=0, le=100)] | None = None  # Amount of ticks since this entity was last hurt by a mob. Counts up from 0 to 100.
    locator_bar_icon: WaypointIcon | None = None
