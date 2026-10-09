"""
Generated from symbols.json for ::java::data::worldgen::processor_list::Processor
Local link to file: generated_symbols/data/worldgen/processor_list/Processor.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from generated_symbols.data.worldgen.processor_list.BlockAge import BlockAge
from generated_symbols.data.worldgen.processor_list.BlockIgnore import BlockIgnore
from generated_symbols.data.worldgen.processor_list.BlockRot import BlockRot
from generated_symbols.data.worldgen.processor_list.Capped import Capped
from generated_symbols.data.worldgen.processor_list.Gravity import Gravity
from generated_symbols.data.worldgen.processor_list.ProtectedBlocks import ProtectedBlocks
from generated_symbols.data.worldgen.processor_list.Rule import Rule
from pydantic import Field


class ProcessorBlockAge(BlockAge):
    processor_type: Literal['minecraft:block_age', 'block_age'] = 'minecraft:block_age'


class ProcessorBlockIgnore(BlockIgnore):
    processor_type: Literal['minecraft:block_ignore', 'block_ignore'] = 'minecraft:block_ignore'


class ProcessorBlockRot(BlockRot):
    processor_type: Literal['minecraft:block_rot', 'block_rot'] = 'minecraft:block_rot'


class ProcessorCapped(Capped):
    processor_type: Literal['minecraft:capped', 'capped'] = 'minecraft:capped'


class ProcessorGravity(Gravity):
    processor_type: Literal['minecraft:gravity', 'gravity'] = 'minecraft:gravity'


class ProcessorProtectedBlocks(ProtectedBlocks):
    processor_type: Literal['minecraft:protected_blocks', 'protected_blocks'] = 'minecraft:protected_blocks'


class ProcessorRule(Rule):
    processor_type: Literal['minecraft:rule', 'rule'] = 'minecraft:rule'


type Processor = Annotated[
    ProcessorBlockAge | ProcessorBlockIgnore | ProcessorBlockRot | ProcessorCapped | ProcessorGravity | ProcessorProtectedBlocks | ProcessorRule,
    Field(discriminator='processor_type'),
]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::Processor": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "processor_type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "worldgen/structure_processor"
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
                                "processor_type"
                            ]
                        }
                    ],
                    "registry": "minecraft:template_processor"
                }
            }
        ]
    }
}

