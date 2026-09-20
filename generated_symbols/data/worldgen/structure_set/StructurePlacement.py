"""
Generated from symbols.json for ::java::data::worldgen::structure_set::StructurePlacement
Local link to file: generated_symbols/data/worldgen/structure_set/StructurePlacement.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.base import GeneratedModel
from generated_symbols.data.worldgen.structure_set.ConcentricRingsPlacement import ConcentricRingsPlacement
from generated_symbols.data.worldgen.structure_set.RandomSpreadPlacement import RandomSpreadPlacement
from minecraft_registry import IdSpec
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.structure_set.ExclusionZone import ExclusionZone
    from generated_symbols.data.worldgen.structure_set.FrequencyReductionMethod import FrequencyReductionMethod


class StructurePlacementUnknown(GeneratedModel):
    type: Annotated[str, IdSpec(registry='worldgen/structure_placement')]
    salt: Annotated[int, Field(ge=0)]
    frequency_reduction_method: FrequencyReductionMethod | None = None
    frequency: Annotated[float, Field(ge=0, le=1)] | None = None
    exclusion_zone: ExclusionZone | None = None
    locate_offset: tuple[Annotated[int, Field(ge=-16, le=16)], Annotated[int, Field(ge=-16, le=16)], Annotated[int, Field(ge=-16, le=16)]] | None = None


class StructurePlacementConcentricRings(ConcentricRingsPlacement):
    type: Literal['minecraft:concentric_rings'] = 'minecraft:concentric_rings'
    salt: Annotated[int, Field(ge=0)]
    frequency_reduction_method: FrequencyReductionMethod | None = None
    frequency: Annotated[float, Field(ge=0, le=1)] | None = None
    exclusion_zone: ExclusionZone | None = None
    locate_offset: tuple[Annotated[int, Field(ge=-16, le=16)], Annotated[int, Field(ge=-16, le=16)], Annotated[int, Field(ge=-16, le=16)]] | None = None


class StructurePlacementRandomSpread(RandomSpreadPlacement):
    type: Literal['minecraft:random_spread'] = 'minecraft:random_spread'
    salt: Annotated[int, Field(ge=0)]
    frequency_reduction_method: FrequencyReductionMethod | None = None
    frequency: Annotated[float, Field(ge=0, le=1)] | None = None
    exclusion_zone: ExclusionZone | None = None
    locate_offset: tuple[Annotated[int, Field(ge=-16, le=16)], Annotated[int, Field(ge=-16, le=16)], Annotated[int, Field(ge=-16, le=16)]] | None = None


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

