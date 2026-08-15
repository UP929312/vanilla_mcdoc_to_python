"""
Generated from symbols.json for ::java::data::worldgen::processor_list::RuleTest
Local link to file: generated_symbols/data/worldgen/processor_list/RuleTest.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.registry.KnownBlockId import KnownBlockId
    from generated_symbols.util.block_state.BlockState import BlockState


@dataclass(kw_only=True)
class RuleTestAllOf:
    predicate_type: Literal['minecraft:all_of']
    rules: list[RuleTest]


@dataclass(kw_only=True)
class RuleTestAnyOf:
    predicate_type: Literal['minecraft:any_of']
    rules: list[RuleTest]


@dataclass(kw_only=True)
class RuleTestBlockMatch:
    predicate_type: Literal['minecraft:block_match']
    block: Annotated[str, IdSpec(registry='block')] | KnownBlockId


@dataclass(kw_only=True)
class RuleTestBlockstateMatch:
    predicate_type: Literal['minecraft:blockstate_match']
    block_state: BlockState


@dataclass(kw_only=True)
class RuleTestHeightMatch:
    predicate_type: Literal['minecraft:height_match']
    min_inclusive: int
    max_inclusive: int


@dataclass(kw_only=True)
class RuleTestNot:
    predicate_type: Literal['minecraft:not']
    rule: RuleTest


@dataclass(kw_only=True)
class RuleTestRandomBlockMatch:
    predicate_type: Literal['minecraft:random_block_match']
    block: Annotated[str, IdSpec(registry='block')] | KnownBlockId
    probability: Annotated[float, 'Range | `0`-`1` | both inclusive']


@dataclass(kw_only=True)
class RuleTestRandomBlockstateMatch:
    predicate_type: Literal['minecraft:random_blockstate_match']
    block_state: BlockState
    probability: Annotated[float, 'Range | `0`-`1` | both inclusive']


@dataclass(kw_only=True)
class RuleTestTagMatch:
    predicate_type: Literal['minecraft:tag_match']
    tag: Annotated[str, IdSpec(registry='block', tags='implicit')] | KnownBlockId


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

