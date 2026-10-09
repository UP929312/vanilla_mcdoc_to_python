"""
Generated from symbols.json for ::java::data::worldgen::processor_list::RuleTest
Local link to file: generated_symbols/data/worldgen/processor_list/RuleTest.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from generated_symbols.data.worldgen.processor_list.BlockMatch import BlockMatch
from generated_symbols.data.worldgen.processor_list.BlockStateMatch import BlockStateMatch
from generated_symbols.data.worldgen.processor_list.CompositeMatch import CompositeMatch
from generated_symbols.data.worldgen.processor_list.HeightMatch import HeightMatch
from generated_symbols.data.worldgen.processor_list.InvertedMatch import InvertedMatch
from generated_symbols.data.worldgen.processor_list.RandomBlockMatch import RandomBlockMatch
from generated_symbols.data.worldgen.processor_list.RandomBlockStateMatch import RandomBlockStateMatch
from generated_symbols.data.worldgen.processor_list.TagMatch import TagMatch
from pydantic import Field


class RuleTestAllOf(CompositeMatch):
    predicate_type: Literal['minecraft:all_of', 'all_of'] = 'minecraft:all_of'


class RuleTestAnyOf(CompositeMatch):
    predicate_type: Literal['minecraft:any_of', 'any_of'] = 'minecraft:any_of'


class RuleTestBlockMatch(BlockMatch):
    predicate_type: Literal['minecraft:block_match', 'block_match'] = 'minecraft:block_match'


class RuleTestBlockstateMatch(BlockStateMatch):
    predicate_type: Literal['minecraft:blockstate_match', 'blockstate_match'] = 'minecraft:blockstate_match'


class RuleTestHeightMatch(HeightMatch):
    predicate_type: Literal['minecraft:height_match', 'height_match'] = 'minecraft:height_match'


class RuleTestNot(InvertedMatch):
    predicate_type: Literal['minecraft:not', 'not'] = 'minecraft:not'


class RuleTestRandomBlockMatch(RandomBlockMatch):
    predicate_type: Literal['minecraft:random_block_match', 'random_block_match'] = 'minecraft:random_block_match'


class RuleTestRandomBlockstateMatch(RandomBlockStateMatch):
    predicate_type: Literal['minecraft:random_blockstate_match', 'random_blockstate_match'] = 'minecraft:random_blockstate_match'


class RuleTestTagMatch(TagMatch):
    predicate_type: Literal['minecraft:tag_match', 'tag_match'] = 'minecraft:tag_match'


type RuleTest = Annotated[
    RuleTestAllOf | RuleTestAnyOf | RuleTestBlockMatch | RuleTestBlockstateMatch | RuleTestHeightMatch | RuleTestNot | RuleTestRandomBlockMatch | RuleTestRandomBlockstateMatch | RuleTestTagMatch,
    Field(discriminator='predicate_type'),
]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::RuleTest": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "predicate_type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "rule_test"
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
                                "predicate_type"
                            ]
                        }
                    ],
                    "registry": "minecraft:rule_test"
                }
            }
        ]
    }
}

