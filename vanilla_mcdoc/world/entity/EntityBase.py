"""
Generated from symbols.json for ::java::world::entity::EntityBase
Local link to file: vanilla_mcdoc/world/entity/EntityBase.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import MinecraftUUID

if TYPE_CHECKING:
    from vanilla_mcdoc.util.text.Text import Text
    from vanilla_mcdoc.world.component.CustomData import CustomData
    from vanilla_mcdoc.world.entity.AnyEntity import AnyEntity


class EntityBase(GeneratedModel):
    Pos: tuple[float, float, float] | None = None
    Motion: tuple[float, float, float] | None = None
    Rotation: tuple[float, float] | None = None  # Rotation in [y-rotation, x-rotation]
    fall_distance: float | None = None  # How far the entity has fallen.
    Fire: int | None = None  # Ticks of fire left, or if negative, ticks until the entity starts to burn.
    Air: int | None = None  # Ticks of air left.
    HasVisualFire: bool | None = None  # Whether the entity has visual fire.
    OnGround: bool | None = None  # Whether the entity is on the ground.
    NoGravity: bool | None = None  # Whether the entity should be effected by gravity.
    Invulnerable: bool | None = None  # Whether the entity is immune to damage.
    invulnerable_time: Annotated[int, Field(ge=0)] | None = None  # Temporary immunity duration of the entity, in ticks.  The entity is immune to damage if `invulnerable_time` > 0 **or** `Invulnerable` is `true`.
    PortalCooldown: int | None = None  # How long until the entity can go through a nether portal.
    UUID: MinecraftUUID | None = None
    CustomName: Text | None = None
    CustomNameVisible: bool | None = None  # Whether the custom name should always be visible.
    Silent: bool | None = None  # Whether the entity should make any sound.
    Passengers: list[AnyEntity] | None = None  # Passengers on the entity.
    Glowing: bool | None = None  # Whether the entity should glow.
    Tags: list[str] | None = None  # Labelling tags on the entity.
    Team: str | None = None  # Team to join when it is spawned.
    data: CustomData | None = None  # Any stored data
    TicksFrozen: int | None = None  # Ticks that this entity has been freezing. Although this tag is defined for all entities, it is actually only used by mobs that are not in the `freeze_immune_entity_types` entity type tag. This increases by one every tick the entity is in powdered snow, and decreases by two when it's out of it.
