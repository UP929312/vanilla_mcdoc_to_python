"""
Generated from symbols.json for ::java::data::loot::function::CustomModelDataStrings
Local link to file: generated_symbols/data/loot/function/CustomModelDataStrings.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

from generated_symbols.data.loot.function.InsertListOperation import InsertListOperation
from generated_symbols.data.loot.function.ReplaceSectionListOperation import ReplaceSectionListOperation


@dataclass(kw_only=True)
class CustomModelDataStringsAppend:
    values: list[str]
    mode: Literal['minecraft:append']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class CustomModelDataStringsInsert(InsertListOperation):
    values: list[str]
    mode: Literal['minecraft:insert']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class CustomModelDataStringsReplaceAll:
    values: list[str]
    mode: Literal['minecraft:replace_all']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class CustomModelDataStringsReplaceSection(ReplaceSectionListOperation):
    values: list[str]
    mode: Literal['minecraft:replace_section']  # Determines how the existing list should be modified.


type CustomModelDataStrings = CustomModelDataStringsAppend | CustomModelDataStringsInsert | CustomModelDataStringsReplaceAll | CustomModelDataStringsReplaceSection


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::CustomModelDataStrings": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "values",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string"
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

