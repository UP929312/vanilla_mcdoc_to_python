"""
Generated from symbols.json for ::java::data::loot::function::ListOperation
Local link to file: generated_symbols/data/loot/function/ListOperation.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated, Literal


@dataclass(kw_only=True)
class ListOperationAppend:
    mode: Literal['minecraft:append']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class ListOperationInsert:
    mode: Literal['minecraft:insert']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset in the list to insert into. Defaults to 0.


@dataclass(kw_only=True)
class ListOperationReplaceAll:
    mode: Literal['minecraft:replace_all']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class ListOperationReplaceSection:
    mode: Literal['minecraft:replace_section']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset of the section to replace. Defaults to 0.
    size: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The size of the section to replace. Defaults to size of the new list.


type ListOperation = ListOperationAppend | ListOperationInsert | ListOperationReplaceAll | ListOperationReplaceSection


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::ListOperation": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Determines how the existing list should be modified.",
                "key": "mode",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::ListOperationMode"
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
                                "mode"
                            ]
                        }
                    ],
                    "registry": "minecraft:list_operation"
                }
            }
        ]
    }
}

