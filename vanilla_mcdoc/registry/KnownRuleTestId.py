"""Known built-in IDs for a generated registry."""
from typing import Literal

type KnownRuleTestId = Literal[
    'minecraft:all_of',
    'minecraft:any_of',
    'minecraft:block_match',
    'minecraft:blockstate_match',
    'minecraft:height_match',
    'minecraft:not',
    'minecraft:random_block_match',
    'minecraft:random_blockstate_match',
    'minecraft:tag_match',
]
