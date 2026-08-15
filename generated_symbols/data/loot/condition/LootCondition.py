"""
Generated from symbols.json for ::java::data::loot::condition::LootCondition
Local link to file: generated_symbols/data/loot/condition/LootCondition.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Any, Literal

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.BlockPredicateState import BlockPredicateState
    from generated_symbols.data.advancement.predicate.DamageSourcePredicate import DamageSourcePredicate
    from generated_symbols.data.advancement.predicate.EntityPredicate import EntityPredicate
    from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate
    from generated_symbols.data.advancement.predicate.LocationPredicate import LocationPredicate
    from generated_symbols.data.enchantment.LevelBasedValue import LevelBasedValue
    from generated_symbols.data.loot.EntityTarget import EntityTarget
    from generated_symbols.data.number_provider.NumberProviderRef import NumberProviderRef
    from generated_symbols.data.predicate.PredicateListRef import PredicateListRef
    from generated_symbols.data.predicate.PredicateRef import PredicateRef
    from generated_symbols.data.util.IntRange import IntRange
    from generated_symbols.data.util.MoonPhase import MoonPhase
    from generated_symbols.data.worldgen.attribute.AmbientParticle import AmbientParticle
    from generated_symbols.data.worldgen.attribute.AmbientSounds import AmbientSounds
    from generated_symbols.data.worldgen.attribute.BackgroundMusic import BackgroundMusic
    from generated_symbols.data.worldgen.attribute.BedRule import BedRule
    from generated_symbols.data.worldgen.attribute.TriState import TriState
    from generated_symbols.data.worldgen.biome.NaturalMobSpawns import NaturalMobSpawns
    from generated_symbols.registry.KnownBlockId import KnownBlockId
    from generated_symbols.registry.KnownEnvironmentAttributeId import KnownEnvironmentAttributeId
    from generated_symbols.util.color.StringARGB import StringARGB
    from generated_symbols.util.color.StringRGB import StringRGB
    from generated_symbols.util.particle.Particle import Particle
    from generated_symbols.world.block.BlockEntity import BlockEntity
    from generated_symbols.world.block.banner.Banner import Banner
    from generated_symbols.world.block.beacon.Beacon import Beacon
    from generated_symbols.world.block.beehive.Beehive import Beehive
    from generated_symbols.world.block.brewing_stand.BrewingStand import BrewingStand
    from generated_symbols.world.block.brushable_block.BrushableBlock import BrushableBlock
    from generated_symbols.world.block.campfire.Campfire import Campfire
    from generated_symbols.world.block.chiseled_bookshelf.ChiseledBookshelf import ChiseledBookshelf
    from generated_symbols.world.block.command_block.CommandBlock import CommandBlock
    from generated_symbols.world.block.comparator.Comparator import Comparator
    from generated_symbols.world.block.conduit.Conduit import Conduit
    from generated_symbols.world.block.container.Container27 import Container27
    from generated_symbols.world.block.container.Container9 import Container9
    from generated_symbols.world.block.container.Hopper import Hopper
    from generated_symbols.world.block.container.Shelf import Shelf
    from generated_symbols.world.block.crafter.Crafter import Crafter
    from generated_symbols.world.block.decorated_pot.DecoratedPot import DecoratedPot
    from generated_symbols.world.block.enchanting_table.EnchantingTable import EnchantingTable
    from generated_symbols.world.block.end_gateway.EndGateway import EndGateway
    from generated_symbols.world.block.furnace.Furnace import Furnace
    from generated_symbols.world.block.head.Skull import Skull
    from generated_symbols.world.block.jigsaw.Jigsaw import Jigsaw
    from generated_symbols.world.block.jukebox.Jukebox import Jukebox
    from generated_symbols.world.block.lectern.Lectern import Lectern
    from generated_symbols.world.block.moving_piston.MovingPiston import MovingPiston
    from generated_symbols.world.block.potent_sulfur.PotentSulfur import PotentSulfur
    from generated_symbols.world.block.sculk_catalyst.SculkCatalyst import SculkCatalyst
    from generated_symbols.world.block.sculk_sensor.SculkSensor import SculkSensor
    from generated_symbols.world.block.sculk_shrieker.SculkShrieker import SculkShrieker
    from generated_symbols.world.block.sign.Sign import Sign
    from generated_symbols.world.block.spawner.Spawner import Spawner
    from generated_symbols.world.block.spawner.TrialSpawner import TrialSpawner
    from generated_symbols.world.block.structure_block.StructureBlock import StructureBlock
    from generated_symbols.world.block.test_block.TestBlock import TestBlock
    from generated_symbols.world.block.test_instance_block.TestInstanceBlock import TestInstanceBlock
    from generated_symbols.world.block.vault.Vault import Vault
    from generated_symbols.world.component.DataComponentExactPredicate import DataComponentExactPredicate
    from generated_symbols.world.component.DataComponentPredicate import DataComponentPredicate


type PropertiesStructBlockStatesNone = dict[str, str]


@dataclass(kw_only=True)
class NbtStructBlockUnknown:
    pass


@dataclass(kw_only=True)
class LootConditionAllOf:
    type: Literal['minecraft:all_of']
    terms: PredicateListRef  # Passes when all of these conditions pass.


@dataclass(kw_only=True)
class LootConditionAlternative:
    type: Literal['minecraft:alternative']
    terms: list[LootCondition]


@dataclass(kw_only=True)
class LootConditionAnyOf:
    type: Literal['minecraft:any_of']
    terms: PredicateListRef  # Passes when any of these conditions pass.


@dataclass(kw_only=True)
class LootConditionBlockStateProperty:
    type: Literal['minecraft:block_state_property']
    block: Annotated[str, IdSpec(registry='block')] | KnownBlockId
    properties: PropertiesStructBlockStatesNone | None = None


@dataclass(kw_only=True)
class LootConditionDamageSourceProperties:
    type: Literal['minecraft:damage_source_properties']
    predicate: DamageSourcePredicate


@dataclass(kw_only=True)
class LootConditionEnchantmentActiveCheck:
    type: Literal['minecraft:enchantment_active_check']
    active: bool


@dataclass(kw_only=True)
class LootConditionEntityProperties:
    type: Literal['minecraft:entity_properties']
    entity: EntityTarget
    predicate: EntityPredicate


@dataclass(kw_only=True)
class LootConditionEntityScores:
    type: Literal['minecraft:entity_scores']
    entity: EntityTarget
    scores: dict[str, IntRange]


@dataclass(kw_only=True)
class LootConditionEnvironmentAttributeCheck:
    type: Literal['minecraft:environment_attribute_check']
    attribute: Annotated[str, IdSpec(registry='environment_attribute')] | KnownEnvironmentAttributeId
    value: Any | AmbientSounds | BackgroundMusic | bool | Annotated[float, 'Range | `0`-`1` | both inclusive'] | Annotated[str, IdSpec(registry='activity')] | BedRule | Annotated[float, 'Range | `0`-`0.9999999` | both inclusive'] | TriState | NaturalMobSpawns | Annotated[float, 'Range | `0`-`15` | both inclusive'] | StringRGB | list[AmbientParticle] | StringARGB | Annotated[float, 'Range | Min `0` and above | inclusive'] | float | Particle | MoonPhase


@dataclass(kw_only=True)
class LootConditionInverted:
    type: Literal['minecraft:inverted']
    term: PredicateRef


@dataclass(kw_only=True)
class LootConditionKilledByPlayer:
    type: Literal['minecraft:killed_by_player']
    inverse: bool | None = None


@dataclass(kw_only=True)
class LootConditionLocationCheck:
    type: Literal['minecraft:location_check']
    predicate: LocationPredicate
    offsetX: int | None = None
    offsetY: int | None = None
    offsetZ: int | None = None


@dataclass(kw_only=True)
class LootConditionMatchBlock:
    type: Literal['minecraft:match_block']
    blocks: Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId | list[Annotated[str, IdSpec(registry='block')] | KnownBlockId] | None = None
    state: BlockPredicateState | None = None
    nbt: str | NbtStructBlockUnknown | Sign | Shelf | Container27 | Beacon | BlockEntity | Beehive | Banner | Furnace | BrewingStand | SculkSensor | Campfire | CommandBlock | ChiseledBookshelf | Comparator | Conduit | Crafter | Skull | DecoratedPot | Container9 | EnchantingTable | EndGateway | Hopper | Jigsaw | Jukebox | Lectern | MovingPiston | PotentSulfur | SculkCatalyst | SculkShrieker | Spawner | StructureBlock | BrushableBlock | TestBlock | TestInstanceBlock | TrialSpawner | Vault | None = None
    components: DataComponentExactPredicate | None = None  # Match exact data component values on the block entity.
    predicates: DataComponentPredicate | None = None  # Test data component values on the block entity.


@dataclass(kw_only=True)
class LootConditionMatchTool:
    type: Literal['minecraft:match_tool']
    predicate: ItemPredicate


@dataclass(kw_only=True)
class LootConditionRandomChance:
    type: Literal['minecraft:random_chance']
    chance: NumberProviderRef  # Clamps to a float between `0` & `1` (inclusive).


@dataclass(kw_only=True)
class LootConditionRandomChanceWithEnchantedBonus:
    type: Literal['minecraft:random_chance_with_enchanted_bonus']
    unenchanted_chance: Annotated[float, 'Range | `0`-`1` | both inclusive']
    enchanted_chance: LevelBasedValue
    enchantment: Annotated[str, IdSpec(registry='enchantment')]


@dataclass(kw_only=True)
class LootConditionRandomChanceWithLooting:
    type: Literal['minecraft:random_chance_with_looting']
    chance: Annotated[float, 'Range | `0`-`1` | both inclusive']
    looting_multiplier: float  # Looting adjustment to the base success rate. Formula is `chance + (looting_level * looting_multiplier)` .


@dataclass(kw_only=True)
class LootConditionReference:
    type: Literal['minecraft:reference']
    name: Annotated[str, IdSpec(registry='predicate')]  # A cyclic reference causes a parsing failure.


@dataclass(kw_only=True)
class LootConditionTableBonus:
    type: Literal['minecraft:table_bonus']
    enchantment: Annotated[str, IdSpec(registry='enchantment')]
    chances: list[Annotated[float, 'Range | `0`-`1` | both inclusive']]  # Probabilities for each enchantment level


@dataclass(kw_only=True)
class LootConditionTimeCheck:
    type: Literal['minecraft:time_check']
    clock: Annotated[str, IdSpec(registry='world_clock')]  # The world clock to check.
    value: IntRange  # Check the current game tick.
    period: int | None = None  # Game tick supplied to `value` check gets modulo-divided by this. For example, if set to 24000, `value` operates on a time period of days.


@dataclass(kw_only=True)
class LootConditionValueCheck:
    type: Literal['minecraft:value_check']
    value: NumberProviderRef  # Clamps to an integer.
    range: IntRange  # Passes when `value` is within this range.


@dataclass(kw_only=True)
class LootConditionWeatherCheck:
    type: Literal['minecraft:weather_check']
    raining: bool | None = None
    thundering: bool | None = None


type LootCondition = LootConditionAllOf | LootConditionAlternative | LootConditionAnyOf | LootConditionBlockStateProperty | LootConditionDamageSourceProperties | LootConditionEnchantmentActiveCheck | LootConditionEntityProperties | LootConditionEntityScores | LootConditionEnvironmentAttributeCheck | LootConditionInverted | LootConditionKilledByPlayer | LootConditionLocationCheck | LootConditionMatchBlock | LootConditionMatchTool | LootConditionRandomChance | LootConditionRandomChanceWithEnchantedBonus | LootConditionRandomChanceWithLooting | LootConditionReference | LootConditionTableBonus | LootConditionTimeCheck | LootConditionValueCheck | LootConditionWeatherCheck


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::condition::LootCondition": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "condition",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::data::loot::LootConditionType",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.16"
                                        }
                                    }
                                },
                                {
                                    "name": "id"
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
                                            "value": "1.16"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "loot_condition_type"
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
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "condition"
                            ]
                        }
                    ],
                    "registry": "minecraft:loot_condition"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
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
                                    "value": "loot_condition_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
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
                    "registry": "minecraft:loot_condition"
                }
            }
        ]
    }
}

