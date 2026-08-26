"""
Generated from symbols.json for ::java::data::loot::function::CustomModelDataFlags
Local link to file: generated_symbols/data/loot/function/CustomModelDataFlags.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated, Literal


@dataclass(kw_only=True)
class CustomModelDataFlagsAppend:
    values: list[bool]
    mode: Literal['minecraft:append']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class CustomModelDataFlagsInsert:
    values: list[bool]
    mode: Literal['minecraft:insert']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | `0` and above | inclusive'] | None = None  # The offset in the list to insert into. Defaults to 0.


@dataclass(kw_only=True)
class CustomModelDataFlagsReplaceAll:
    values: list[bool]
    mode: Literal['minecraft:replace_all']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class CustomModelDataFlagsReplaceSection:
    values: list[bool]
    mode: Literal['minecraft:replace_section']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | `0` and above | inclusive'] | None = None  # The offset of the section to replace. Defaults to 0.
    size: Annotated[int, 'Range | `0` and above | inclusive'] | None = None  # The size of the section to replace. Defaults to size of the new list.


type CustomModelDataFlags = CustomModelDataFlagsAppend | CustomModelDataFlagsInsert | CustomModelDataFlagsReplaceAll | CustomModelDataFlagsReplaceSection


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::CustomModelDataFlags": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "values",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "boolean"
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

