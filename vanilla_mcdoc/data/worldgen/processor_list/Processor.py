"""
Generated from symbols.json for ::java::data::worldgen::processor_list::Processor
Local link to file: vanilla_mcdoc/data/worldgen/processor_list/Processor.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import GeneratedModel, tag_of
from vanilla_mcdoc.data.worldgen.processor_list.BlockAge import BlockAge
from vanilla_mcdoc.data.worldgen.processor_list.BlockIgnore import BlockIgnore
from vanilla_mcdoc.data.worldgen.processor_list.BlockRot import BlockRot
from vanilla_mcdoc.data.worldgen.processor_list.Capped import Capped
from vanilla_mcdoc.data.worldgen.processor_list.Gravity import Gravity
from vanilla_mcdoc.data.worldgen.processor_list.ProtectedBlocks import ProtectedBlocks
from vanilla_mcdoc.data.worldgen.processor_list.Rule import Rule


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


class ProcessorRule2(Rule):
    processor_type: Literal['minecraft:rule', 'rule'] = 'minecraft:rule'


class ProcessorBlackstoneReplace(GeneratedModel):
    processor_type: Literal['minecraft:blackstone_replace', 'blackstone_replace'] = 'minecraft:blackstone_replace'


class ProcessorJigsawReplacement(GeneratedModel):
    processor_type: Literal['minecraft:jigsaw_replacement', 'jigsaw_replacement'] = 'minecraft:jigsaw_replacement'


class ProcessorLavaSubmergedBlock(GeneratedModel):
    processor_type: Literal['minecraft:lava_submerged_block', 'lava_submerged_block'] = 'minecraft:lava_submerged_block'


class ProcessorNop(GeneratedModel):
    processor_type: Literal['minecraft:nop', 'nop'] = 'minecraft:nop'


type Processor = Annotated[
    Annotated[ProcessorBlockAge, Tag('minecraft:block_age')]
    | Annotated[ProcessorBlockIgnore, Tag('minecraft:block_ignore')]
    | Annotated[ProcessorBlockRot, Tag('minecraft:block_rot')]
    | Annotated[ProcessorCapped, Tag('minecraft:capped')]
    | Annotated[ProcessorGravity, Tag('minecraft:gravity')]
    | Annotated[ProcessorProtectedBlocks, Tag('minecraft:protected_blocks')]
    | Annotated[ProcessorRule2, Tag('minecraft:rule')]
    | Annotated[ProcessorBlackstoneReplace, Tag('minecraft:blackstone_replace')]
    | Annotated[ProcessorJigsawReplacement, Tag('minecraft:jigsaw_replacement')]
    | Annotated[ProcessorLavaSubmergedBlock, Tag('minecraft:lava_submerged_block')]
    | Annotated[ProcessorNop, Tag('minecraft:nop')],
    Discriminator(tag_of('processor_type')),
]
