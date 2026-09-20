"""
Generated from symbols.json for ::java::util::particle::Particle
Local link to file: generated_symbols/util/particle/Particle.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from generated_symbols.base import GeneratedModel
from generated_symbols.util.particle.BlockParticle import BlockParticle
from generated_symbols.util.particle.DragonBreathParticle import DragonBreathParticle
from generated_symbols.util.particle.DustColorTransitionParticle import DustColorTransitionParticle
from generated_symbols.util.particle.DustParticle import DustParticle
from generated_symbols.util.particle.EffectParticle import EffectParticle
from generated_symbols.util.particle.EntityEffectParticle import EntityEffectParticle
from generated_symbols.util.particle.FlashParticle import FlashParticle
from generated_symbols.util.particle.GeyserBaseParticle import GeyserBaseParticle
from generated_symbols.util.particle.GeyserParticle import GeyserParticle
from generated_symbols.util.particle.ItemParticle import ItemParticle
from generated_symbols.util.particle.SculkChargeParticle import SculkChargeParticle
from generated_symbols.util.particle.ShriekParticle import ShriekParticle
from generated_symbols.util.particle.TintedLeavesParticle import TintedLeavesParticle
from generated_symbols.util.particle.TrailParticle import TrailParticle
from generated_symbols.util.particle.VibrationParticle import VibrationParticle
from minecraft_registry import IdSpec


class ParticleNone(GeneratedModel):
    type: Annotated[str, IdSpec(registry='particle_type')]


class ParticleUnknown(GeneratedModel):
    type: Annotated[str, IdSpec(registry='particle_type')]


class ParticleBlock(BlockParticle):
    type: Literal['minecraft:block'] = 'minecraft:block'


class ParticleBlockCrumble(BlockParticle):
    type: Literal['minecraft:block_crumble'] = 'minecraft:block_crumble'


class ParticleBlockMarker(BlockParticle):
    type: Literal['minecraft:block_marker'] = 'minecraft:block_marker'


class ParticleDragonBreath(DragonBreathParticle):
    type: Literal['minecraft:dragon_breath'] = 'minecraft:dragon_breath'


class ParticleDust(DustParticle):
    type: Literal['minecraft:dust'] = 'minecraft:dust'


class ParticleDustColorTransition(DustColorTransitionParticle):
    type: Literal['minecraft:dust_color_transition'] = 'minecraft:dust_color_transition'


class ParticleDustPillar(BlockParticle):
    type: Literal['minecraft:dust_pillar'] = 'minecraft:dust_pillar'


class ParticleEffect(EffectParticle):
    type: Literal['minecraft:effect'] = 'minecraft:effect'


class ParticleEntityEffect(EntityEffectParticle):
    type: Literal['minecraft:entity_effect'] = 'minecraft:entity_effect'


class ParticleFallingDust(BlockParticle):
    type: Literal['minecraft:falling_dust'] = 'minecraft:falling_dust'


class ParticleFlash(FlashParticle):
    type: Literal['minecraft:flash'] = 'minecraft:flash'


class ParticleGeyser(GeyserParticle):
    type: Literal['minecraft:geyser'] = 'minecraft:geyser'


class ParticleGeyserBase(GeyserBaseParticle):
    type: Literal['minecraft:geyser_base'] = 'minecraft:geyser_base'


class ParticleGeyserPlume(GeyserParticle):
    type: Literal['minecraft:geyser_plume'] = 'minecraft:geyser_plume'


class ParticleGeyserPoof(GeyserBaseParticle):
    type: Literal['minecraft:geyser_poof'] = 'minecraft:geyser_poof'


class ParticleInstantEffect(EffectParticle):
    type: Literal['minecraft:instant_effect'] = 'minecraft:instant_effect'


class ParticleItem(ItemParticle):
    type: Literal['minecraft:item'] = 'minecraft:item'


class ParticleSculkCharge(SculkChargeParticle):
    type: Literal['minecraft:sculk_charge'] = 'minecraft:sculk_charge'


class ParticleShriek(ShriekParticle):
    type: Literal['minecraft:shriek'] = 'minecraft:shriek'


class ParticleTintedLeaves(TintedLeavesParticle):
    type: Literal['minecraft:tinted_leaves'] = 'minecraft:tinted_leaves'


class ParticleTrail(TrailParticle):
    type: Literal['minecraft:trail'] = 'minecraft:trail'


class ParticleVibration(VibrationParticle):
    type: Literal['minecraft:vibration'] = 'minecraft:vibration'


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

