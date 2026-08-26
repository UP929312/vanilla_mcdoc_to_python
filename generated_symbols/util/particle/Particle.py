"""
Generated from symbols.json for ::java::util::particle::Particle
Local link to file: generated_symbols/util/particle/Particle.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated, Literal

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


@dataclass(kw_only=True)
class ParticleNone:
    type: Annotated[str, IdSpec(registry='particle_type')]


@dataclass(kw_only=True)
class ParticleUnknown:
    type: Annotated[str, IdSpec(registry='particle_type')]


@dataclass(kw_only=True)
class ParticleBlock(BlockParticle):
    type: Literal['minecraft:block'] = 'minecraft:block'


@dataclass(kw_only=True)
class ParticleBlockCrumble(BlockParticle):
    type: Literal['minecraft:block_crumble'] = 'minecraft:block_crumble'


@dataclass(kw_only=True)
class ParticleBlockMarker(BlockParticle):
    type: Literal['minecraft:block_marker'] = 'minecraft:block_marker'


@dataclass(kw_only=True)
class ParticleDragonBreath(DragonBreathParticle):
    type: Literal['minecraft:dragon_breath'] = 'minecraft:dragon_breath'


@dataclass(kw_only=True)
class ParticleDust(DustParticle):
    type: Literal['minecraft:dust'] = 'minecraft:dust'


@dataclass(kw_only=True)
class ParticleDustColorTransition(DustColorTransitionParticle):
    type: Literal['minecraft:dust_color_transition'] = 'minecraft:dust_color_transition'


@dataclass(kw_only=True)
class ParticleDustPillar(BlockParticle):
    type: Literal['minecraft:dust_pillar'] = 'minecraft:dust_pillar'


@dataclass(kw_only=True)
class ParticleEffect(EffectParticle):
    type: Literal['minecraft:effect'] = 'minecraft:effect'


@dataclass(kw_only=True)
class ParticleEntityEffect(EntityEffectParticle):
    type: Literal['minecraft:entity_effect'] = 'minecraft:entity_effect'


@dataclass(kw_only=True)
class ParticleFallingDust(BlockParticle):
    type: Literal['minecraft:falling_dust'] = 'minecraft:falling_dust'


@dataclass(kw_only=True)
class ParticleFlash(FlashParticle):
    type: Literal['minecraft:flash'] = 'minecraft:flash'


@dataclass(kw_only=True)
class ParticleGeyser(GeyserParticle):
    type: Literal['minecraft:geyser'] = 'minecraft:geyser'


@dataclass(kw_only=True)
class ParticleGeyserBase(GeyserBaseParticle):
    type: Literal['minecraft:geyser_base'] = 'minecraft:geyser_base'


@dataclass(kw_only=True)
class ParticleGeyserPlume(GeyserParticle):
    type: Literal['minecraft:geyser_plume'] = 'minecraft:geyser_plume'


@dataclass(kw_only=True)
class ParticleGeyserPoof(GeyserBaseParticle):
    type: Literal['minecraft:geyser_poof'] = 'minecraft:geyser_poof'


@dataclass(kw_only=True)
class ParticleInstantEffect(EffectParticle):
    type: Literal['minecraft:instant_effect'] = 'minecraft:instant_effect'


@dataclass(kw_only=True)
class ParticleItem(ItemParticle):
    type: Literal['minecraft:item'] = 'minecraft:item'


@dataclass(kw_only=True)
class ParticleSculkCharge(SculkChargeParticle):
    type: Literal['minecraft:sculk_charge'] = 'minecraft:sculk_charge'


@dataclass(kw_only=True)
class ParticleShriek(ShriekParticle):
    type: Literal['minecraft:shriek'] = 'minecraft:shriek'


@dataclass(kw_only=True)
class ParticleTintedLeaves(TintedLeavesParticle):
    type: Literal['minecraft:tinted_leaves'] = 'minecraft:tinted_leaves'


@dataclass(kw_only=True)
class ParticleTrail(TrailParticle):
    type: Literal['minecraft:trail'] = 'minecraft:trail'


@dataclass(kw_only=True)
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

