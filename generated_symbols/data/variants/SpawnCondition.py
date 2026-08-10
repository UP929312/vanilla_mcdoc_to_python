"""
Generated from symbols.json for ::java::data::variants::SpawnCondition
Local link to file: generated_symbols/data/variants/SpawnCondition.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


@dataclass(kw_only=True)
class SpawnConditionBiome:
    type: Literal['minecraft:biome']
    biomes: Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')] | list[Annotated[str, IdSpec(registry='worldgen/biome')]]  # Checks if the entity is spawning in specific biomes.


@dataclass(kw_only=True)
class SpawnConditionMoonBrightness:
    type: Literal['minecraft:moon_brightness']
    range: MinMaxBounds[float] | float  # Checks if the current moon brightness is within a certain range.


@dataclass(kw_only=True)
class SpawnConditionStructure:
    type: Literal['minecraft:structure']
    structures: Annotated[str, IdSpec(registry='worldgen/structure', tags='allowed')] | list[Annotated[str, IdSpec(registry='worldgen/structure')]]  # Checks if the entity is spawning in specific structures.


type SpawnCondition = SpawnConditionBiome | SpawnConditionMoonBrightness | SpawnConditionStructure


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::variants::SpawnCondition": {
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
                                    "value": "spawn_condition_type"
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
                    "registry": "minecraft:spawn_condition"
                }
            }
        ]
    }
}

