"""
Generated from symbols.json for ::java::data::loot::function::CustomModelDataStrings
Local link to file: generated_symbols/data/loot/function/CustomModelDataStrings.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated, Literal


@dataclass(kw_only=True)
class CustomModelDataStringsAppend:
    values: list[str]
    mode: Literal['minecraft:append']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class CustomModelDataStringsInsert:
    values: list[str]
    mode: Literal['minecraft:insert']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset in the list to insert into. Defaults to 0.


@dataclass(kw_only=True)
class CustomModelDataStringsReplaceAll:
    values: list[str]
    mode: Literal['minecraft:replace_all']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class CustomModelDataStringsReplaceSection:
    values: list[str]
    mode: Literal['minecraft:replace_section']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset of the section to replace. Defaults to 0.
    size: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The size of the section to replace. Defaults to size of the new list.


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

