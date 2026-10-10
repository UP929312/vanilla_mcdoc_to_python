"""
Generated from symbols.json for ::java::data::enchantment::effect::ExplodeEntityEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect/ExplodeEntityEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.LevelBasedValue import LevelBasedValue
    from vanilla_mcdoc.data.enchantment.effect.BlockInteraction import BlockInteraction
    from vanilla_mcdoc.data.enchantment.effect.ExplosionParticleInfo import ExplosionParticleInfo
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId
    from vanilla_mcdoc.util.FlatWeightedList import FlatWeightedList
    from vanilla_mcdoc.util.particle.Particle import Particle


class ExplodeEntityEffect(GeneratedModel):
    attribute_to_user: bool | None = None  # Whether the explosion should be attributed to the user of the enchanted tool.
    damage_type: Annotated[str, IdSpec(registry='damage_type')] | None = None  # If omitted, no damage is dealt by the explosion.
    immune_blocks: Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId | list[Annotated[str, IdSpec(registry='block')] | KnownBlockId] | None = None  # List of Blocks or hash-prefixed Block Tag specifying which blocks fully block the explosion.
    knockback_multiplier: LevelBasedValue | None = None  # If omitted, constant value `1` is applied.
    offset: tuple[float, float, float] | None = None  # Relative coordinates to offset the explosion by. Defaults to `[0, 0, 0]`.
    radius: LevelBasedValue
    create_fire: bool | None = None  # Whether fire is placed within the explosion radius.
    block_interaction: BlockInteraction  # Whether the explosion has special effects on blocks.
    small_particle: Particle
    large_particle: Particle
    block_particles: FlatWeightedList[ExplosionParticleInfo] | None = None
    sound: SoundEventRef
