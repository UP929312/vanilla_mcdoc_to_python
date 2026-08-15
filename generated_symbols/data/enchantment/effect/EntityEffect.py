"""
Generated from symbols.json for ::java::data::enchantment::effect::EntityEffect
Local link to file: generated_symbols/data/enchantment/effect/EntityEffect.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.data.enchantment.effect.ReplaceBlockEntityEffect import ReplaceBlockEntityEffect
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.LevelBasedValue import LevelBasedValue
    from generated_symbols.data.enchantment.effect.BlockInteraction import BlockInteraction
    from generated_symbols.data.enchantment.effect.ExplosionParticleInfo import ExplosionParticleInfo
    from generated_symbols.data.enchantment.effect.ParticlePosition import ParticlePosition
    from generated_symbols.data.enchantment.effect.ParticleVelocity import ParticleVelocity
    from generated_symbols.data.util.SoundEventRef import SoundEventRef
    from generated_symbols.data.worldgen.FloatProvider import FloatProvider
    from generated_symbols.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProvider import BlockStateProvider
    from generated_symbols.registry.KnownBlockId import KnownBlockId
    from generated_symbols.util.particle.Particle import Particle


type PropertiesStructDataComponentBlockStateBlockItemStatesNone = dict[str, str]


@dataclass(kw_only=True)
class EntityEffectAllOf:
    type: Literal['minecraft:all_of']
    effects: Annotated[list[EntityEffect], 'Length = 1 (inclusive) and above']


@dataclass(kw_only=True)
class EntityEffectApplyExhaustion:
    type: Literal['minecraft:apply_exhaustion']
    amount: LevelBasedValue  # The amount of exhaustion to apply to player.


@dataclass(kw_only=True)
class EntityEffectApplyImpulse:
    type: Literal['minecraft:apply_impulse']
    direction: tuple[float, float, float]  # Impulse direction in local coordinates (the same used by `tp @s ^ ^ ^`).  `[left, upward, forward]`
    coordinate_scale: tuple[float, float, float]  # The multipler to apply to the computed impulse direction.  `[x, y, z]`
    magnitude: LevelBasedValue  # The scale of the impulse.


@dataclass(kw_only=True)
class EntityEffectApplyMobEffect:
    type: Literal['minecraft:apply_mob_effect']
    to_apply: Annotated[str, IdSpec(registry='mob_effect', tags='allowed')] | list[Annotated[str, IdSpec(registry='mob_effect')]]  # If multiple mob effects are specified, a random effect is selected.
    min_duration: LevelBasedValue
    max_duration: LevelBasedValue
    min_amplifier: LevelBasedValue
    max_amplifier: LevelBasedValue


@dataclass(kw_only=True)
class EntityEffectChangeItemDamage:
    type: Literal['minecraft:change_item_damage']
    amount: LevelBasedValue  # Damage to apply to the enchanted item. Negative values will repair the item. The change is not applied to items held by players in creative mode.


@dataclass(kw_only=True)
class EntityEffectDamageEntity:
    type: Literal['minecraft:damage_entity']
    damage_type: Annotated[str, IdSpec(registry='damage_type')]
    min_damage: LevelBasedValue  # Amount of damage is randomized within the given min/max span.
    max_damage: LevelBasedValue


@dataclass(kw_only=True)
class EntityEffectDamageItem:
    type: Literal['minecraft:damage_item']
    amount: LevelBasedValue  # Damage to apply to the enchanted item. The damage is not applied to items held by players in creative mode.


@dataclass(kw_only=True)
class EntityEffectExplode:
    type: Literal['minecraft:explode']
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
    block_particles: list[ExplosionParticleInfo] | None = None
    sound: SoundEventRef


@dataclass(kw_only=True)
class EntityEffectIgnite:
    type: Literal['minecraft:ignite']
    duration: LevelBasedValue  # Seconds the fire should last.


@dataclass(kw_only=True)
class EntityEffectPlaySound:
    type: Literal['minecraft:play_sound']
    sound: SoundEventRef | Annotated[list[SoundEventRef], 'Length = 1-255 (both inclusive)']
    volume: FloatProvider[Annotated[float, 'Range | `1e-05`-`10` | both inclusive']] | Annotated[float, 'Range | `1e-05`-`10` | both inclusive']
    pitch: FloatProvider[Annotated[float, 'Range | `1e-05`-`2` | both inclusive']] | Annotated[float, 'Range | `1e-05`-`2` | both inclusive']


@dataclass(kw_only=True)
class EntityEffectReplaceBlock:
    type: Literal['minecraft:replace_block']
    block_state: BlockStateProvider
    offset: tuple[int, int, int] | None = None  # Relative coordinates to offset the placed block by. Defaults to `[0, 0, 0]`.
    predicate: BlockPredicate | None = None  # If omitted, all block types are replaced.
    trigger_game_event: Annotated[str, IdSpec(registry='game_event')] | None = None  # Defaults to no game event dispatched.


@dataclass(kw_only=True)
class EntityEffectReplaceDisk(ReplaceBlockEntityEffect):
    type: Literal['minecraft:replace_disk']
    offset: tuple[int, int, int] | None = None  # Relative coordinates to offset the center of the cylinder by. Defaults to `[0, 0, 0]`.
    radius: LevelBasedValue
    height: LevelBasedValue


@dataclass(kw_only=True)
class EntityEffectRunFunction:
    type: Literal['minecraft:run_function']
    function: Annotated[str, IdSpec(registry='function')]


@dataclass(kw_only=True)
class EntityEffectSetBlockProperties:
    type: Literal['minecraft:set_block_properties']
    properties: PropertiesStructDataComponentBlockStateBlockItemStatesNone
    offset: tuple[int, int, int] | None = None  # Relative coordinates to offset the block by. Defaults to `[0, 0, 0]`.
    trigger_game_event: Annotated[str, IdSpec(registry='game_event')] | None = None  # Defaults to no game event dispatched.


@dataclass(kw_only=True)
class EntityEffectSpawnParticles:
    type: Literal['minecraft:spawn_particles']
    particle: Particle
    horizontal_position: ParticlePosition
    vertical_position: ParticlePosition
    horizontal_velocity: ParticleVelocity
    vertical_velocity: ParticleVelocity
    speed: float | None = None


@dataclass(kw_only=True)
class EntityEffectSummonEntity:
    type: Literal['minecraft:summon_entity']
    entity: Annotated[str, IdSpec(registry='entity_type', tags='allowed')] | list[Annotated[str, IdSpec(registry='entity_type')]]  # If multiple entity types are specified, a random entity type is selected.
    join_team: bool | None = None  # Whether the summoned entity should join the team of the owner of the Enchanted Item.


type EntityEffect = EntityEffectAllOf | EntityEffectApplyExhaustion | EntityEffectApplyImpulse | EntityEffectApplyMobEffect | EntityEffectChangeItemDamage | EntityEffectDamageEntity | EntityEffectDamageItem | EntityEffectExplode | EntityEffectIgnite | EntityEffectPlaySound | EntityEffectReplaceBlock | EntityEffectReplaceDisk | EntityEffectRunFunction | EntityEffectSetBlockProperties | EntityEffectSpawnParticles | EntityEffectSummonEntity


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::EntityEffect": {
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
                                    "value": "enchantment_entity_effect_type"
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
                    "registry": "minecraft:entity_effect"
                }
            }
        ]
    }
}

