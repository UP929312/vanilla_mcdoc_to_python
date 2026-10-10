"""
Generated from symbols.json for ::java::world::entity::area_effect_cloud::AreaEffectCloud
Local link to file: vanilla_mcdoc/world/entity/area_effect_cloud/AreaEffectCloud.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec, MinecraftUUID
from vanilla_mcdoc.world.entity.EntityBase import EntityBase

if TYPE_CHECKING:
    from vanilla_mcdoc.util.particle.Particle import Particle
    from vanilla_mcdoc.world.component.item.PotionContents import PotionContents


class AreaEffectCloud(EntityBase):
    Age: int | None = None  # Number of ticks it has existed. Controls when it will despawn; when greater than `Duration + WaitTime`.
    Color: int | None = None  # Color of the particles. calculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive
    Duration: int | None = None  # Maximum number of ticks until it will disappear after `WaitTime` is done
    ReapplicationDelay: int | None = None  # Number of ticks until the effects are reapplied.
    WaitTime: int | None = None  # Number of ticks until it appears.
    DurationOnUse: int | None = None  # Amount the duration changes when it is active.
    Owner: MinecraftUUID | None = None
    Radius: float | None = None  # Radius of the particles & effect applications.
    RadiusOnUse: float | None = None  # Change in the radius when it is used.
    RadiusPerTick: float | None = None  # Change in the radius per tick.
    custom_particle: Particle | None = None  # If present, the particle that the area effect cloud displays instead of the default `entity_effect` particle based on the potion contents.
    potion_contents: PotionContents | Annotated[str, IdSpec(registry='potion')] | None = None
    potion_duration_scale: float | None = None  # The duration of the potion effect applied is scaled by this factor. Defaults to `1`. Will be `0.25` when throwing lingering potions.
