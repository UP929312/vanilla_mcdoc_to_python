"""
Generated from symbols.json for ::java::data::worldgen::processor_list::RuleTest
Local link to file: generated_symbols/data/worldgen/processor_list/RuleTest.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

from generated_symbols.data.worldgen.processor_list.BlockMatch import BlockMatch
from generated_symbols.data.worldgen.processor_list.BlockStateMatch import BlockStateMatch
from generated_symbols.data.worldgen.processor_list.CompositeMatch import CompositeMatch
from generated_symbols.data.worldgen.processor_list.HeightMatch import HeightMatch
from generated_symbols.data.worldgen.processor_list.InvertedMatch import InvertedMatch
from generated_symbols.data.worldgen.processor_list.RandomBlockMatch import RandomBlockMatch
from generated_symbols.data.worldgen.processor_list.RandomBlockStateMatch import RandomBlockStateMatch
from generated_symbols.data.worldgen.processor_list.TagMatch import TagMatch


@dataclass(kw_only=True)
class RuleTestAllOf(CompositeMatch):
    predicate_type: Literal['minecraft:all_of']


@dataclass(kw_only=True)
class RuleTestAnyOf(CompositeMatch):
    predicate_type: Literal['minecraft:any_of']


@dataclass(kw_only=True)
class RuleTestBlockMatch(BlockMatch):
    predicate_type: Literal['minecraft:block_match']


@dataclass(kw_only=True)
class RuleTestBlockstateMatch(BlockStateMatch):
    predicate_type: Literal['minecraft:blockstate_match']


@dataclass(kw_only=True)
class RuleTestHeightMatch(HeightMatch):
    predicate_type: Literal['minecraft:height_match']


@dataclass(kw_only=True)
class RuleTestNot(InvertedMatch):
    predicate_type: Literal['minecraft:not']


@dataclass(kw_only=True)
class RuleTestRandomBlockMatch(RandomBlockMatch):
    predicate_type: Literal['minecraft:random_block_match']


@dataclass(kw_only=True)
class RuleTestRandomBlockstateMatch(RandomBlockStateMatch):
    predicate_type: Literal['minecraft:random_blockstate_match']


@dataclass(kw_only=True)
class RuleTestTagMatch(TagMatch):
    predicate_type: Literal['minecraft:tag_match']


type RuleTest = RuleTestAllOf | RuleTestAnyOf | RuleTestBlockMatch | RuleTestBlockstateMatch | RuleTestHeightMatch | RuleTestNot | RuleTestRandomBlockMatch | RuleTestRandomBlockstateMatch | RuleTestTagMatch


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

