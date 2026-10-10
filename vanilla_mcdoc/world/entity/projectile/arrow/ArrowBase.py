"""
Generated from symbols.json for ::java::world::entity::projectile::arrow::ArrowBase
Local link to file: vanilla_mcdoc/world/entity/projectile/arrow/ArrowBase.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.world.entity.projectile.ProjectileBase import ProjectileBase

if TYPE_CHECKING:
    from vanilla_mcdoc.util.block_state.BlockState import BlockState
    from vanilla_mcdoc.world.entity.projectile.arrow.Pickup import Pickup
    from vanilla_mcdoc.world.item.ItemStack import ItemStack


class ArrowBase(ProjectileBase):
    shake: int | None = None  # Shake it creates.
    pickup: Pickup | None = None  # How players can pick up it.
    life: int | None = None  # Ticks since it last moved.
    damage: float | None = None  # Damage it should deal.
    inGround: bool | None = None  # Whether it is in the ground.
    inBlockState: BlockState | None = None  # Block it is in.
    crit: bool | None = None  # Whether it should do critical damage.
    weapon: ItemStack | None = None  # The item which has shot this arrow.
    PierceLevel: int | None = None  # Number of entities it can pass through.
    SoundEvent: Annotated[str, IdSpec(registry='sound_event')] | None = None  # Sound event to play when it hits something.  Can only be vanilla sound events
    item: ItemStack | None = None
