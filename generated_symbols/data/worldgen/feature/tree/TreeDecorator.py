"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::TreeDecorator
Local link to file: generated_symbols/data/worldgen/feature/tree/TreeDecorator.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProvider import BlockStateProvider
    from generated_symbols.util.direction.Direction import Direction


@dataclass(kw_only=True)
class TreeDecoratorAlterGround:
    type: Literal['minecraft:alter_ground']
    provider: BlockStateProvider


@dataclass(kw_only=True)
class TreeDecoratorAttachedToLeaves:
    type: Literal['minecraft:attached_to_leaves']
    probability: Annotated[float, 'Range | `0`-`1` | both inclusive']
    exclusion_radius_xz: Annotated[int, 'Range | `0`-`16` | both inclusive']
    exclusion_radius_y: Annotated[int, 'Range | `0`-`16` | both inclusive']
    required_empty_blocks: Annotated[int, 'Range | `1`-`16` | both inclusive']
    block_provider: BlockStateProvider
    directions: Annotated[list[Direction], 'Length = 1 (inclusive) and above']


@dataclass(kw_only=True)
class TreeDecoratorAttachedToLogs:
    type: Literal['minecraft:attached_to_logs']
    probability: Annotated[float, 'Range | `0`-`1` | both inclusive']
    block_provider: BlockStateProvider
    directions: Annotated[list[Direction], 'Length = 1 (inclusive) and above']


@dataclass(kw_only=True)
class TreeDecoratorBeehive:
    type: Literal['minecraft:beehive']
    probability: Annotated[float, 'Range | `0`-`1` | both inclusive']


@dataclass(kw_only=True)
class TreeDecoratorCocoa:
    type: Literal['minecraft:cocoa']
    probability: Annotated[float, 'Range | `0`-`1` | both inclusive']


@dataclass(kw_only=True)
class TreeDecoratorCreakingHeart:
    type: Literal['minecraft:creaking_heart']
    probability: Annotated[float, 'Range | `0`-`1` | both inclusive']


@dataclass(kw_only=True)
class TreeDecoratorLeaveVine:
    type: Literal['minecraft:leave_vine']
    probability: Annotated[float, 'Range | `0`-`1` | both inclusive']


@dataclass(kw_only=True)
class TreeDecoratorPaleMoss:
    type: Literal['minecraft:pale_moss']
    leaves_probability: Annotated[float, 'Range | `0`-`1` | both inclusive']
    trunk_probability: Annotated[float, 'Range | `0`-`1` | both inclusive']
    ground_probability: Annotated[float, 'Range | `0`-`1` | both inclusive']


@dataclass(kw_only=True)
class TreeDecoratorPlaceOnGround:
    type: Literal['minecraft:place_on_ground']
    tries: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # Defaults to `128`.
    radius: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # Defaults to `2`.
    height: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # Defaults to `1`.
    block_state_provider: BlockStateProvider  # The block to place on the ground.


@dataclass(kw_only=True)
class TreeDecoratorShelfMushroom:
    type: Literal['minecraft:shelf_mushroom']
    probability: Annotated[float, 'Range | `0`-`1` | both inclusive']


type TreeDecorator = TreeDecoratorAlterGround | TreeDecoratorAttachedToLeaves | TreeDecoratorAttachedToLogs | TreeDecoratorBeehive | TreeDecoratorCocoa | TreeDecoratorCreakingHeart | TreeDecoratorLeaveVine | TreeDecoratorPaleMoss | TreeDecoratorPlaceOnGround | TreeDecoratorShelfMushroom


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::TreeDecorator": {
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
                                    "value": "worldgen/tree_decorator_type"
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
                    "registry": "minecraft:tree_decorator"
                }
            }
        ]
    }
}

