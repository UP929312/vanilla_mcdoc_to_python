"""
Generated from symbols.json for ::java::data::advancement::predicate::EntitySubPredicate
Local link to file: generated_symbols/data/advancement/predicate/EntitySubPredicate.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.BlockPredicate import BlockPredicate
    from generated_symbols.data.advancement.predicate.EntityPredicate import EntityPredicate
    from generated_symbols.data.advancement.predicate.FluidPredicate import FluidPredicate
    from generated_symbols.data.advancement.predicate.GameMode import GameMode
    from generated_symbols.data.advancement.predicate.StatisticPredicate import StatisticPredicate
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


@dataclass(kw_only=True)
class PositionStruct:
    x: MinMaxBounds[float] | float | None = None
    y: MinMaxBounds[float] | float | None = None
    z: MinMaxBounds[float] | float | None = None


@dataclass(kw_only=True)
class LightStruct:
    light: MinMaxBounds[Annotated[int, 'Range | `0`-`15` | both inclusive']] | Annotated[int, 'Range | `0`-`15` | both inclusive'] | None = None


type AdvancementsStructValueStruct = dict[str, bool]


@dataclass(kw_only=True)
class InputStruct:
    forward: bool | None = None
    backward: bool | None = None
    left: bool | None = None
    right: bool | None = None
    jump: bool | None = None
    sneak: bool | None = None
    sprint: bool | None = None


@dataclass(kw_only=True)
class FoodStruct:
    level: MinMaxBounds[int] | int | None = None
    saturation: MinMaxBounds[float] | float | None = None


@dataclass(kw_only=True)
class EntitySubPredicateComponents:
    type: Literal['minecraft:components']


@dataclass(kw_only=True)
class EntitySubPredicateDistance:
    type: Literal['minecraft:distance']
    x: MinMaxBounds[float] | float | None = None
    y: MinMaxBounds[float] | float | None = None
    z: MinMaxBounds[float] | float | None = None
    absolute: MinMaxBounds[float] | float | None = None
    horizontal: MinMaxBounds[float] | float | None = None


@dataclass(kw_only=True)
class EntitySubPredicateEffects:
    type: Literal['minecraft:effects']


@dataclass(kw_only=True)
class EntitySubPredicateEntityTags:
    type: Literal['minecraft:entity_tags']
    any_of: list[str] | None = None  # Must have at least one of the listed tags.
    all_of: list[str] | None = None  # Must have all the listed tags.
    none_of: list[str] | None = None  # Must have none of the listed tags.


@dataclass(kw_only=True)
class EntitySubPredicateEntityType:
    type: Literal['minecraft:entity_type']


@dataclass(kw_only=True)
class EntitySubPredicateEquipment:
    type: Literal['minecraft:equipment']


@dataclass(kw_only=True)
class EntitySubPredicateFlags:
    type: Literal['minecraft:flags']
    is_on_fire: bool | None = None
    is_sneaking: bool | None = None
    is_sprinting: bool | None = None
    is_swimming: bool | None = None
    is_baby: bool | None = None
    is_on_ground: bool | None = None
    is_flying: bool | None = None
    is_in_water: bool | None = None
    is_fall_flying: bool | None = None


@dataclass(kw_only=True)
class EntitySubPredicateLocation:
    type: Literal['minecraft:location']
    position: PositionStruct | None = None
    biomes: Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')] | list[Annotated[str, IdSpec(registry='worldgen/biome')]] | None = None
    structures: Annotated[str, IdSpec(registry='worldgen/structure', tags='allowed')] | list[Annotated[str, IdSpec(registry='worldgen/structure')]] | None = None
    dimension: Annotated[str, IdSpec(registry='dimension')] | None = None
    light: LightStruct | None = None  # Calculated using: `max(sky-darkening, block)`.
    block: BlockPredicate | None = None
    fluid: FluidPredicate | None = None
    smokey: bool | None = None  # Whether the block is above (5 blocks or less) a campfire or soul campfire.
    can_see_sky: bool | None = None  # Whether the location has the maximum possible level of sky light


@dataclass(kw_only=True)
class EntitySubPredicateMovement:
    type: Literal['minecraft:movement']
    x: MinMaxBounds[float] | float | None = None
    y: MinMaxBounds[float] | float | None = None
    z: MinMaxBounds[float] | float | None = None
    speed: MinMaxBounds[float] | float | None = None
    horizontal_speed: MinMaxBounds[float] | float | None = None
    vertical_speed: MinMaxBounds[float] | float | None = None
    fall_distance: MinMaxBounds[float] | float | None = None


@dataclass(kw_only=True)
class EntitySubPredicateMovementAffectedBy:
    type: Literal['minecraft:movement_affected_by']
    position: PositionStruct | None = None
    biomes: Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')] | list[Annotated[str, IdSpec(registry='worldgen/biome')]] | None = None
    structures: Annotated[str, IdSpec(registry='worldgen/structure', tags='allowed')] | list[Annotated[str, IdSpec(registry='worldgen/structure')]] | None = None
    dimension: Annotated[str, IdSpec(registry='dimension')] | None = None
    light: LightStruct | None = None  # Calculated using: `max(sky-darkening, block)`.
    block: BlockPredicate | None = None
    fluid: FluidPredicate | None = None
    smokey: bool | None = None  # Whether the block is above (5 blocks or less) a campfire or soul campfire.
    can_see_sky: bool | None = None  # Whether the location has the maximum possible level of sky light


@dataclass(kw_only=True)
class EntitySubPredicateNbt:
    type: Literal['minecraft:nbt']


@dataclass(kw_only=True)
class EntitySubPredicatePassenger:
    type: Literal['minecraft:passenger']


@dataclass(kw_only=True)
class EntitySubPredicatePeriodicTick:
    type: Literal['minecraft:periodic_tick']


@dataclass(kw_only=True)
class EntitySubPredicatePredicates:
    type: Literal['minecraft:predicates']


@dataclass(kw_only=True)
class EntitySubPredicateSlots:
    type: Literal['minecraft:slots']


@dataclass(kw_only=True)
class EntitySubPredicateSteppingOn:
    type: Literal['minecraft:stepping_on']
    position: PositionStruct | None = None
    biomes: Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')] | list[Annotated[str, IdSpec(registry='worldgen/biome')]] | None = None
    structures: Annotated[str, IdSpec(registry='worldgen/structure', tags='allowed')] | list[Annotated[str, IdSpec(registry='worldgen/structure')]] | None = None
    dimension: Annotated[str, IdSpec(registry='dimension')] | None = None
    light: LightStruct | None = None  # Calculated using: `max(sky-darkening, block)`.
    block: BlockPredicate | None = None
    fluid: FluidPredicate | None = None
    smokey: bool | None = None  # Whether the block is above (5 blocks or less) a campfire or soul campfire.
    can_see_sky: bool | None = None  # Whether the location has the maximum possible level of sky light


@dataclass(kw_only=True)
class EntitySubPredicateTargetedEntity:
    type: Literal['minecraft:targeted_entity']


@dataclass(kw_only=True)
class EntitySubPredicateTeam:
    type: Literal['minecraft:team']


@dataclass(kw_only=True)
class EntitySubPredicateTypeSpecificCubeMob:
    type: Literal['minecraft:type_specific/cube_mob']
    size: MinMaxBounds[int] | int | None = None


@dataclass(kw_only=True)
class EntitySubPredicateTypeSpecificFishingHook:
    type: Literal['minecraft:type_specific/fishing_hook']
    in_open_water: bool | None = None


@dataclass(kw_only=True)
class EntitySubPredicateTypeSpecificLightning:
    type: Literal['minecraft:type_specific/lightning']
    blocks_set_on_fire: MinMaxBounds[int] | int | None = None
    entity_struck: EntityPredicate | None = None


@dataclass(kw_only=True)
class EntitySubPredicateTypeSpecificPlayer:
    type: Literal['minecraft:type_specific/player']
    advancements: dict[Annotated[str, IdSpec(registry='advancement')], bool | AdvancementsStructValueStruct] | None = None
    gamemode: list[GameMode] | None = None
    level: MinMaxBounds[int] | int | None = None  # Experience/XP level.
    recipes: dict[Annotated[str, IdSpec(registry='recipe')], bool] | None = None
    stats: list[StatisticPredicate] | None = None
    looking_at: EntityPredicate | None = None
    input: InputStruct | None = None  # Checks the movement keys of the player.
    food: FoodStruct | None = None


@dataclass(kw_only=True)
class EntitySubPredicateTypeSpecificRaider:
    type: Literal['minecraft:type_specific/raider']
    has_raid: bool | None = None
    is_captain: bool | None = None


@dataclass(kw_only=True)
class EntitySubPredicateTypeSpecificSheep:
    type: Literal['minecraft:type_specific/sheep']
    sheared: bool | None = None


@dataclass(kw_only=True)
class EntitySubPredicateVehicle:
    type: Literal['minecraft:vehicle']


type EntitySubPredicate = EntitySubPredicateComponents | EntitySubPredicateDistance | EntitySubPredicateEffects | EntitySubPredicateEntityTags | EntitySubPredicateEntityType | EntitySubPredicateEquipment | EntitySubPredicateFlags | EntitySubPredicateLocation | EntitySubPredicateMovement | EntitySubPredicateMovementAffectedBy | EntitySubPredicateNbt | EntitySubPredicatePassenger | EntitySubPredicatePeriodicTick | EntitySubPredicatePredicates | EntitySubPredicateSlots | EntitySubPredicateSteppingOn | EntitySubPredicateTargetedEntity | EntitySubPredicateTeam | EntitySubPredicateTypeSpecificCubeMob | EntitySubPredicateTypeSpecificFishingHook | EntitySubPredicateTypeSpecificLightning | EntitySubPredicateTypeSpecificPlayer | EntitySubPredicateTypeSpecificRaider | EntitySubPredicateTypeSpecificSheep | EntitySubPredicateVehicle


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::EntitySubPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::data::advancement::predicate::SpecificType",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.20.5"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.20.5"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "entity_sub_predicate_type"
                                        }
                                    }
                                }
                            ]
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
                    "registry": "minecraft:entity_sub_predicate"
                }
            }
        ]
    }
}

