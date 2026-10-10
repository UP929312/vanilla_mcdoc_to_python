"""
Generated from symbols.json for ::java::util::particle::Particle
Local link to file: vanilla_mcdoc/util/particle/Particle.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.util.particle.BlockParticle import BlockParticle
from vanilla_mcdoc.util.particle.DragonBreathParticle import DragonBreathParticle
from vanilla_mcdoc.util.particle.DustColorTransitionParticle import DustColorTransitionParticle
from vanilla_mcdoc.util.particle.DustParticle import DustParticle
from vanilla_mcdoc.util.particle.EffectParticle import EffectParticle
from vanilla_mcdoc.util.particle.EntityEffectParticle import EntityEffectParticle
from vanilla_mcdoc.util.particle.FlashParticle import FlashParticle
from vanilla_mcdoc.util.particle.GeyserBaseParticle import GeyserBaseParticle
from vanilla_mcdoc.util.particle.GeyserParticle import GeyserParticle
from vanilla_mcdoc.util.particle.ItemParticle import ItemParticle
from vanilla_mcdoc.util.particle.SculkChargeParticle import SculkChargeParticle
from vanilla_mcdoc.util.particle.ShriekParticle import ShriekParticle
from vanilla_mcdoc.util.particle.TintedLeavesParticle import TintedLeavesParticle
from vanilla_mcdoc.util.particle.TrailParticle import TrailParticle
from vanilla_mcdoc.util.particle.VibrationParticle import VibrationParticle


class ParticleNone(GeneratedModel):
    type: Annotated[str, IdSpec(registry='particle_type')]


class ParticleUnknown(GeneratedModel):
    type: Annotated[str, IdSpec(registry='particle_type')]


class ParticleBlock(BlockParticle):
    type: Literal['minecraft:block', 'block'] = 'minecraft:block'


class ParticleBlockCrumble(BlockParticle):
    type: Literal['minecraft:block_crumble', 'block_crumble'] = 'minecraft:block_crumble'


class ParticleBlockMarker(BlockParticle):
    type: Literal['minecraft:block_marker', 'block_marker'] = 'minecraft:block_marker'


class ParticleDragonBreath(DragonBreathParticle):
    type: Literal['minecraft:dragon_breath', 'dragon_breath'] = 'minecraft:dragon_breath'


class ParticleDust(DustParticle):
    type: Literal['minecraft:dust', 'dust'] = 'minecraft:dust'


class ParticleDustColorTransition(DustColorTransitionParticle):
    type: Literal['minecraft:dust_color_transition', 'dust_color_transition'] = 'minecraft:dust_color_transition'


class ParticleDustPillar(BlockParticle):
    type: Literal['minecraft:dust_pillar', 'dust_pillar'] = 'minecraft:dust_pillar'


class ParticleEffect(EffectParticle):
    type: Literal['minecraft:effect', 'effect'] = 'minecraft:effect'


class ParticleEntityEffect(EntityEffectParticle):
    type: Literal['minecraft:entity_effect', 'entity_effect'] = 'minecraft:entity_effect'


class ParticleFallingDust(BlockParticle):
    type: Literal['minecraft:falling_dust', 'falling_dust'] = 'minecraft:falling_dust'


class ParticleFlash(FlashParticle):
    type: Literal['minecraft:flash', 'flash'] = 'minecraft:flash'


class ParticleGeyser(GeyserParticle):
    type: Literal['minecraft:geyser', 'geyser'] = 'minecraft:geyser'


class ParticleGeyserBase(GeyserBaseParticle):
    type: Literal['minecraft:geyser_base', 'geyser_base'] = 'minecraft:geyser_base'


class ParticleGeyserPlume(GeyserParticle):
    type: Literal['minecraft:geyser_plume', 'geyser_plume'] = 'minecraft:geyser_plume'


class ParticleGeyserPoof(GeyserBaseParticle):
    type: Literal['minecraft:geyser_poof', 'geyser_poof'] = 'minecraft:geyser_poof'


class ParticleInstantEffect(EffectParticle):
    type: Literal['minecraft:instant_effect', 'instant_effect'] = 'minecraft:instant_effect'


class ParticleItem(ItemParticle):
    type: Literal['minecraft:item', 'item'] = 'minecraft:item'


class ParticleSculkCharge(SculkChargeParticle):
    type: Literal['minecraft:sculk_charge', 'sculk_charge'] = 'minecraft:sculk_charge'


class ParticleShriek(ShriekParticle):
    type: Literal['minecraft:shriek', 'shriek'] = 'minecraft:shriek'


class ParticleTintedLeaves(TintedLeavesParticle):
    type: Literal['minecraft:tinted_leaves', 'tinted_leaves'] = 'minecraft:tinted_leaves'


class ParticleTrail(TrailParticle):
    type: Literal['minecraft:trail', 'trail'] = 'minecraft:trail'


class ParticleVibration(VibrationParticle):
    type: Literal['minecraft:vibration', 'vibration'] = 'minecraft:vibration'


type Particle = ParticleNone | ParticleUnknown | ParticleBlock | ParticleBlockCrumble | ParticleBlockMarker | ParticleDragonBreath | ParticleDust | ParticleDustColorTransition | ParticleDustPillar | ParticleEffect | ParticleEntityEffect | ParticleFallingDust | ParticleFlash | ParticleGeyser | ParticleGeyserBase | ParticleGeyserPlume | ParticleGeyserPoof | ParticleInstantEffect | ParticleItem | ParticleSculkCharge | ParticleShriek | ParticleTintedLeaves | ParticleTrail | ParticleVibration


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::particle::Particle": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "particle_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:particle"
                }
            }
        ]
    }
}
