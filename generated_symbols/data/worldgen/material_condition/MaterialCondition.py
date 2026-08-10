"""
Generated from symbols.json for ::java::data::worldgen::material_condition::MaterialCondition
Local link to file: generated_symbols/data/worldgen/material_condition/MaterialCondition.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.CaveSurface import CaveSurface
    from generated_symbols.data.worldgen.VerticalAnchor import VerticalAnchor
    from generated_symbols.data.worldgen.material_condition.MaterialConditionRef import MaterialConditionRef


@dataclass(kw_only=True)
class MaterialConditionBiome:
    type: Literal['minecraft:biome']
    biome_is: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]


@dataclass(kw_only=True)
class MaterialConditionNoiseThreshold:
    type: Literal['minecraft:noise_threshold']
    noise: Annotated[str, IdSpec(registry='worldgen/noise')]
    min_threshold: float
    max_threshold: float
    is_3d: bool | None = None  # Defaults to `false`.


@dataclass(kw_only=True)
class MaterialConditionNot:
    type: Literal['minecraft:not']
    invert: MaterialConditionRef


@dataclass(kw_only=True)
class MaterialConditionStoneDepth:
    type: Literal['minecraft:stone_depth']
    offset: int
    surface_type: CaveSurface
    add_surface_depth: bool
    secondary_depth_range: int


@dataclass(kw_only=True)
class MaterialConditionVerticalGradient:
    type: Literal['minecraft:vertical_gradient']
    random_name: str
    true_at_and_below: VerticalAnchor
    false_at_and_above: VerticalAnchor


@dataclass(kw_only=True)
class MaterialConditionWater:
    type: Literal['minecraft:water']
    offset: int
    surface_depth_multiplier: Annotated[int, 'Range | `-20`-`20` | both inclusive']
    add_stone_depth: bool


@dataclass(kw_only=True)
class MaterialConditionYAbove:
    type: Literal['minecraft:y_above']
    anchor: VerticalAnchor
    surface_depth_multiplier: Annotated[int, 'Range | `-20`-`20` | both inclusive']
    add_stone_depth: bool


type MaterialCondition = MaterialConditionBiome | MaterialConditionNoiseThreshold | MaterialConditionNot | MaterialConditionStoneDepth | MaterialConditionVerticalGradient | MaterialConditionWater | MaterialConditionYAbove


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::material_condition::MaterialCondition": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
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
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "worldgen/material_condition"
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
                                            "value": "26.3"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "worldgen/material_condition_type"
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
                    "registry": "minecraft:material_condition"
                }
            }
        ]
    }
}

