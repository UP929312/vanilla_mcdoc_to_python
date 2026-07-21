# Generated from symbols.json for ::java::data::worldgen::structure_set::StructurePlacement
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.structure_set.ExclusionZone import ExclusionZone
    from generated_symbols.data.worldgen.structure_set.FrequencyReductionMethod import FrequencyReductionMethod


@dataclass(kw_only=True)
class StructurePlacement:
    type: str
    salt: Annotated[int, 'Range | Min `0` and above | inclusive']
    frequency_reduction_method: FrequencyReductionMethod | None = None
    frequency: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None
    exclusion_zone: ExclusionZone | None = None
    locate_offset: tuple[Annotated[int, 'Range | `-16`-`16` | both inclusive'], Annotated[int, 'Range | `-16`-`16` | both inclusive'], Annotated[int, 'Range | `-16`-`16` | both inclusive']] | None = None


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

