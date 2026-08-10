"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::FeatureSize
Local link to file: generated_symbols/data/worldgen/feature/tree/FeatureSize.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated, Literal


@dataclass(kw_only=True)
class FeatureSizeThreeLayersFeatureSize:
    type: Literal['minecraft:three_layers_feature_size']
    min_clipped_height: Annotated[float, 'Range | `0`-`80` | both inclusive'] | None = None
    limit: Annotated[int, 'Range | `0`-`80` | both inclusive'] | None = None
    upper_limit: Annotated[int, 'Range | `0`-`80` | both inclusive'] | None = None
    lower_size: Annotated[int, 'Range | `0`-`16` | both inclusive'] | None = None
    middle_size: Annotated[int, 'Range | `0`-`16` | both inclusive'] | None = None
    upper_size: Annotated[int, 'Range | `0`-`16` | both inclusive'] | None = None


@dataclass(kw_only=True)
class FeatureSizeTwoLayersFeatureSize:
    type: Literal['minecraft:two_layers_feature_size']
    min_clipped_height: Annotated[float, 'Range | `0`-`80` | both inclusive'] | None = None
    limit: Annotated[int, 'Range | `0`-`81` | both inclusive'] | None = None
    lower_size: Annotated[int, 'Range | `0`-`16` | both inclusive'] | None = None
    upper_size: Annotated[int, 'Range | `0`-`16` | both inclusive'] | None = None


type FeatureSize = FeatureSizeThreeLayersFeatureSize | FeatureSizeTwoLayersFeatureSize


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::FeatureSize": {
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
                                    "value": "worldgen/feature_size_type"
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
                    "registry": "minecraft:feature_size"
                }
            }
        ]
    }
}

