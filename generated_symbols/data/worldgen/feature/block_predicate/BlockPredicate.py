"""
Generated from symbols.json for ::java::data::worldgen::feature::block_predicate::BlockPredicate
Local link to file: generated_symbols/data/worldgen/feature/block_predicate/BlockPredicate.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.data.worldgen.feature.block_predicate.PredicateOffset import PredicateOffset
from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.VerticalAnchor import VerticalAnchor
    from generated_symbols.util.block_state.BlockState import BlockState
    from generated_symbols.util.direction.Direction import Direction


@dataclass(kw_only=True)
class BlockPredicateAllOf:
    type: Literal['minecraft:all_of']
    predicates: list[BlockPredicate]


@dataclass(kw_only=True)
class BlockPredicateAnyOf:
    type: Literal['minecraft:any_of']
    predicates: list[BlockPredicate]


@dataclass(kw_only=True)
class BlockPredicateHasSturdyFace(PredicateOffset):
    type: Literal['minecraft:has_sturdy_face']
    direction: Direction


@dataclass(kw_only=True)
class BlockPredicateHeightRange:
    type: Literal['minecraft:height_range']
    min_inclusive: VerticalAnchor
    max_inclusive: VerticalAnchor


@dataclass(kw_only=True)
class BlockPredicateInsideWorldBounds(PredicateOffset):
    type: Literal['minecraft:inside_world_bounds']


@dataclass(kw_only=True)
class BlockPredicateMatchingBiomes:
    type: Literal['minecraft:matching_biomes']
    biomes: Annotated[str, IdSpec(registry='biome', tags='allowed')] | list[Annotated[str, IdSpec(registry='biome')]]


@dataclass(kw_only=True)
class BlockPredicateMatchingBlockTag(PredicateOffset):
    type: Literal['minecraft:matching_block_tag']
    tag: Annotated[str, IdSpec(registry='block', tags='implicit')]


@dataclass(kw_only=True)
class BlockPredicateMatchingBlocks(PredicateOffset):
    type: Literal['minecraft:matching_blocks']
    blocks: list[Annotated[str, IdSpec(registry='block')]] | Annotated[str, IdSpec(registry='block', tags='allowed')]


@dataclass(kw_only=True)
class BlockPredicateMatchingFluids(PredicateOffset):
    type: Literal['minecraft:matching_fluids']
    fluids: list[Annotated[str, IdSpec(registry='fluid')]] | Annotated[str, IdSpec(registry='fluid', tags='allowed')]


@dataclass(kw_only=True)
class BlockPredicateNot:
    type: Literal['minecraft:not']
    predicate: BlockPredicate


@dataclass(kw_only=True)
class BlockPredicateUnobstructed:
    type: Literal['minecraft:unobstructed']
    offset: tuple[int, int, int] | None = None


@dataclass(kw_only=True)
class BlockPredicateWouldSurvive(PredicateOffset):
    type: Literal['minecraft:would_survive']
    state: BlockState


type BlockPredicate = BlockPredicateAllOf | BlockPredicateAnyOf | BlockPredicateHasSturdyFace | BlockPredicateHeightRange | BlockPredicateInsideWorldBounds | BlockPredicateMatchingBiomes | BlockPredicateMatchingBlockTag | BlockPredicateMatchingBlocks | BlockPredicateMatchingFluids | BlockPredicateNot | BlockPredicateUnobstructed | BlockPredicateWouldSurvive


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::block_predicate::BlockPredicate": {
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
                                    "value": "block_predicate_type"
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
                    "registry": "minecraft:block_predicate"
                }
            }
        ]
    }
}

