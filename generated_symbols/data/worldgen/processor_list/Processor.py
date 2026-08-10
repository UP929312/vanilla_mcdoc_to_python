"""
Generated from symbols.json for ::java::data::worldgen::processor_list::Processor
Local link to file: generated_symbols/data/worldgen/processor_list/Processor.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.HeightmapType import HeightmapType
    from generated_symbols.data.worldgen.IntProvider import IntProvider
    from generated_symbols.data.worldgen.processor_list.ProcessorRule import ProcessorRule
    from generated_symbols.util.block_state.BlockState import BlockState


@dataclass(kw_only=True)
class ProcessorBlockAge:
    processor_type: Literal['minecraft:block_age']
    mossiness: float


@dataclass(kw_only=True)
class ProcessorBlockIgnore:
    processor_type: Literal['minecraft:block_ignore']
    blocks: list[BlockState]


@dataclass(kw_only=True)
class ProcessorBlockRot:
    processor_type: Literal['minecraft:block_rot']
    integrity: Annotated[float, 'Range | `0`-`1` | both inclusive']
    rottable_blocks: list[Annotated[str, IdSpec(registry='block')]] | Annotated[str, IdSpec(registry='block', tags='allowed')] | None = None


@dataclass(kw_only=True)
class ProcessorCapped:
    processor_type: Literal['minecraft:capped']
    delegate: Processor
    limit: IntProvider[Annotated[int, 'Range | Min `0` and above | inclusive']] | Annotated[int, 'Range | Min `0` and above | inclusive']


@dataclass(kw_only=True)
class ProcessorGravity:
    processor_type: Literal['minecraft:gravity']
    heightmap: HeightmapType
    offset: int


@dataclass(kw_only=True)
class ProcessorProtectedBlocks:
    processor_type: Literal['minecraft:protected_blocks']
    value: Annotated[str, IdSpec(registry='block', tags='allowed')] | list[Annotated[str, IdSpec(registry='block')]]


@dataclass(kw_only=True)
class ProcessorRule:
    processor_type: Literal['minecraft:rule']
    rules: list[ProcessorRule]


type Processor = ProcessorBlockAge | ProcessorBlockIgnore | ProcessorBlockRot | ProcessorCapped | ProcessorGravity | ProcessorProtectedBlocks | ProcessorRule


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

