"""
Generated from symbols.json for ::java::util::particle::Particle
Local link to file: generated_symbols/util/particle/Particle.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.util.particle.VibrationParticleData import VibrationParticleData
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.registry.KnownBlockId import KnownBlockId
    from generated_symbols.util.block_state.BlockState import BlockState
    from generated_symbols.util.color.RGB import RGB
    from generated_symbols.util.color.RGBA import RGBA
    from generated_symbols.util.particle.DustColor import DustColor
    from generated_symbols.util.particle.TranslucentParticle import TranslucentParticle
    from generated_symbols.world.item.ItemStackTemplate import ItemStackTemplate


@dataclass(kw_only=True)
class ParticleNone:
    type: Annotated[str, IdSpec(registry='particle_type')]


@dataclass(kw_only=True)
class ParticleUnknown:
    type: Annotated[str, IdSpec(registry='particle_type')]


@dataclass(kw_only=True)
class ParticleBlock:
    type: Literal['minecraft:block']
    block_state: Annotated[str, IdSpec(registry='block')] | KnownBlockId | BlockState


@dataclass(kw_only=True)
class ParticleBlockCrumble:
    type: Literal['minecraft:block_crumble']
    block_state: Annotated[str, IdSpec(registry='block')] | KnownBlockId | BlockState


@dataclass(kw_only=True)
class ParticleBlockMarker:
    type: Literal['minecraft:block_marker']
    block_state: Annotated[str, IdSpec(registry='block')] | KnownBlockId | BlockState


@dataclass(kw_only=True)
class ParticleDragonBreath:
    type: Literal['minecraft:dragon_breath']
    power: float | None = None  # Multiplier of initial velocity. Defaults to 1.0


@dataclass(kw_only=True)
class ParticleDust:
    type: Literal['minecraft:dust']
    color: DustColor
    scale: Annotated[float, 'Range | `0.01`-`4` | both inclusive']


@dataclass(kw_only=True)
class ParticleDustColorTransition:
    type: Literal['minecraft:dust_color_transition']
    from_color: DustColor
    to_color: DustColor
    scale: Annotated[float, 'Range | `0.01`-`4` | both inclusive']


@dataclass(kw_only=True)
class ParticleDustPillar:
    type: Literal['minecraft:dust_pillar']
    block_state: Annotated[str, IdSpec(registry='block')] | KnownBlockId | BlockState


@dataclass(kw_only=True)
class ParticleEffect:
    type: Literal['minecraft:effect']
    power: float | None = None  # Multiplier of initial velocity. Defaults to 1.0
    color: RGB | None = None


@dataclass(kw_only=True)
class ParticleEntityEffect:
    type: Literal['minecraft:entity_effect']
    color: TranslucentParticle


@dataclass(kw_only=True)
class ParticleFallingDust:
    type: Literal['minecraft:falling_dust']
    block_state: Annotated[str, IdSpec(registry='block')] | KnownBlockId | BlockState


@dataclass(kw_only=True)
class ParticleFlash:
    type: Literal['minecraft:flash']
    color: TranslucentParticle


@dataclass(kw_only=True)
class ParticleGeyser:
    type: Literal['minecraft:geyser']
    water_blocks: Annotated[int, 'Range | Min `1` and above | inclusive']  # Scales the particle size and its burst impulse.


@dataclass(kw_only=True)
class ParticleGeyserBase:
    type: Literal['minecraft:geyser_base']
    water_blocks: Annotated[int, 'Range | Min `1` and above | inclusive']  # Scales the particle size and its burst impulse.
    burst_impulse_base: float  # Scales the initial burst impulse


@dataclass(kw_only=True)
class ParticleGeyserPlume:
    type: Literal['minecraft:geyser_plume']
    water_blocks: Annotated[int, 'Range | Min `1` and above | inclusive']  # Scales the particle size and its burst impulse.


@dataclass(kw_only=True)
class ParticleGeyserPoof:
    type: Literal['minecraft:geyser_poof']
    water_blocks: Annotated[int, 'Range | Min `1` and above | inclusive']  # Scales the particle size and its burst impulse.
    burst_impulse_base: float  # Scales the initial burst impulse


@dataclass(kw_only=True)
class ParticleInstantEffect:
    type: Literal['minecraft:instant_effect']
    power: float | None = None  # Multiplier of initial velocity. Defaults to 1.0
    color: RGB | None = None


@dataclass(kw_only=True)
class ParticleItem:
    type: Literal['minecraft:item']
    item: ItemStackTemplate


@dataclass(kw_only=True)
class ParticleSculkCharge:
    type: Literal['minecraft:sculk_charge']
    roll: float  # Angle the particle texture is rotated to, measured in radians (π ~ 3.14 for 180° clockwise, negative for counter clockwise).


@dataclass(kw_only=True)
class ParticleShriek:
    type: Literal['minecraft:shriek']
    delay: Annotated[int, 'Range | Min `0` and above | inclusive']  # Ticks until the particle renders.


@dataclass(kw_only=True)
class ParticleTintedLeaves:
    type: Literal['minecraft:tinted_leaves']
    color: RGBA


@dataclass(kw_only=True)
class ParticleTrail:
    type: Literal['minecraft:trail']
    target: tuple[float, float, float]
    color: RGB
    duration: Annotated[int, 'Range | Min `1` and above | inclusive']


@dataclass(kw_only=True)
class ParticleVibration(VibrationParticleData):
    type: Literal['minecraft:vibration']


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

