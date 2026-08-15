"""
Generated from symbols.json for ::java::data::worldgen::structure_set::StructurePlacement
Local link to file: generated_symbols/data/worldgen/structure_set/StructurePlacement.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.structure_set.ExclusionZone import ExclusionZone
    from generated_symbols.data.worldgen.structure_set.FrequencyReductionMethod import FrequencyReductionMethod
    from generated_symbols.data.worldgen.structure_set.SpreadType import SpreadType


@dataclass(kw_only=True)
class StructurePlacementUnknown:
    type: Annotated[str, IdSpec(registry='worldgen/structure_placement')]
    salt: Annotated[int, 'Range | Min `0` and above | inclusive']
    frequency_reduction_method: FrequencyReductionMethod | None = None
    frequency: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None
    exclusion_zone: ExclusionZone | None = None
    locate_offset: tuple[Annotated[int, 'Range | `-16`-`16` | both inclusive'], Annotated[int, 'Range | `-16`-`16` | both inclusive'], Annotated[int, 'Range | `-16`-`16` | both inclusive']] | None = None


@dataclass(kw_only=True)
class StructurePlacementConcentricRings:
    type: Literal['minecraft:concentric_rings']
    salt: Annotated[int, 'Range | Min `0` and above | inclusive']
    distance: Annotated[int, 'Range | `0`-`1023` | both inclusive']
    spread: Annotated[int, 'Range | `0`-`1023` | both inclusive']
    count: Annotated[int, 'Range | `1`-`4095` | both inclusive']
    preferred_biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    frequency_reduction_method: FrequencyReductionMethod | None = None
    frequency: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None
    exclusion_zone: ExclusionZone | None = None
    locate_offset: tuple[Annotated[int, 'Range | `-16`-`16` | both inclusive'], Annotated[int, 'Range | `-16`-`16` | both inclusive'], Annotated[int, 'Range | `-16`-`16` | both inclusive']] | None = None


@dataclass(kw_only=True)
class StructurePlacementRandomSpread:
    type: Literal['minecraft:random_spread']
    salt: Annotated[int, 'Range | Min `0` and above | inclusive']
    spacing: Annotated[int, 'Range | `0`-`4096` | both inclusive']  # Average distance in chunks between two structures of this type.
    separation: Annotated[int, 'Range | `0`-`4096` | both inclusive']  # Minimum distance in chunks between two structures of this type.
    frequency_reduction_method: FrequencyReductionMethod | None = None
    frequency: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None
    exclusion_zone: ExclusionZone | None = None
    locate_offset: tuple[Annotated[int, 'Range | `-16`-`16` | both inclusive'], Annotated[int, 'Range | `-16`-`16` | both inclusive'], Annotated[int, 'Range | `-16`-`16` | both inclusive']] | None = None
    spread_type: SpreadType | None = None


type StructurePlacement = StructurePlacementUnknown | StructurePlacementConcentricRings | StructurePlacementRandomSpread


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure_set::StructurePlacement": {
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
                                    "value": "worldgen/structure_placement"
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
                    "registry": "minecraft:structure_placement"
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
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "salt",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
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
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "frequency_reduction_method",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::structure_set::FrequencyReductionMethod"
                },
                "optional": True
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
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "frequency",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "exclusion_zone",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::structure_set::ExclusionZone"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "locate_offset",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "int",
                        "valueRange": {
                            "kind": 0,
                            "min": -16,
                            "max": 16
                        }
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                },
                "optional": True
            }
        ]
    }
}

