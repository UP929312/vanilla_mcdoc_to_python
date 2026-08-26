"""
Generated from symbols.json for ::java::data::loot::function::CustomModelDataFloats
Local link to file: generated_symbols/data/loot/function/CustomModelDataFloats.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from generated_symbols.data.loot.function.InsertListOperation import InsertListOperation
from generated_symbols.data.loot.function.ReplaceSectionListOperation import ReplaceSectionListOperation

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.NumberProviderRef import NumberProviderRef


@dataclass(kw_only=True)
class CustomModelDataFloatsAppend:
    values: list[NumberProviderRef]
    mode: Literal['minecraft:append'] = 'minecraft:append'  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class CustomModelDataFloatsInsert(InsertListOperation):
    values: list[NumberProviderRef]
    mode: Literal['minecraft:insert'] = 'minecraft:insert'  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class CustomModelDataFloatsReplaceAll:
    values: list[NumberProviderRef]
    mode: Literal['minecraft:replace_all'] = 'minecraft:replace_all'  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class CustomModelDataFloatsReplaceSection(ReplaceSectionListOperation):
    values: list[NumberProviderRef]
    mode: Literal['minecraft:replace_section'] = 'minecraft:replace_section'  # Determines how the existing list should be modified.


type CustomModelDataFloats = CustomModelDataFloatsAppend | CustomModelDataFloatsInsert | CustomModelDataFloatsReplaceAll | CustomModelDataFloatsReplaceSection


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::CustomModelDataFloats": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "values",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::number_provider::NumberProviderRef"
                    }
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::ListOperation"
                }
            }
        ]
    }
}

