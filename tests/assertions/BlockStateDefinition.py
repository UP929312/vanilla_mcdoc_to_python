# ~~~ WHAT ARE WE TESTING ~~~

# Top-level dataclasses emitted by unions retain two blank lines between declarations.

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::assets::block_state_definition::BlockStateDefinition
Local link to file: generated_symbols/assets/block_state_definition/BlockStateDefinition.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.block_state_definition.ModelVariant import ModelVariant
    from generated_symbols.assets.block_state_definition.MultiPartCondition import MultiPartCondition


@dataclass(kw_only=True)
class MultipartStruct:
    apply: ModelVariant
    when: MultiPartCondition | None = None  # One condition or an array where at least one condition must apply.


@dataclass(kw_only=True)
class BlockStateDefinitionStruct1:
    variants: dict[str, ModelVariant]


@dataclass(kw_only=True)
class BlockStateDefinitionStruct2:
    multipart: list[MultipartStruct]


type BlockStateDefinition = BlockStateDefinitionStruct1 | BlockStateDefinitionStruct2
