"""
Generated from symbols.json for ::java::data::loot::function::CustomModelDataColors
Local link to file: generated_symbols/data/loot/function/CustomModelDataColors.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.NumberProviderRef import NumberProviderRef
    from generated_symbols.util.color.RGB import RGB


@dataclass(kw_only=True)
class CustomModelDataColorsAppend:
    values: list[NumberProviderRef | RGB]
    mode: Literal['minecraft:append']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class CustomModelDataColorsInsert:
    values: list[NumberProviderRef | RGB]
    mode: Literal['minecraft:insert']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset in the list to insert into. Defaults to 0.


@dataclass(kw_only=True)
class CustomModelDataColorsReplaceAll:
    values: list[NumberProviderRef | RGB]
    mode: Literal['minecraft:replace_all']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class CustomModelDataColorsReplaceSection:
    values: list[NumberProviderRef | RGB]
    mode: Literal['minecraft:replace_section']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset of the section to replace. Defaults to 0.
    size: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The size of the section to replace. Defaults to size of the new list.


type CustomModelDataColors = CustomModelDataColorsAppend | CustomModelDataColorsInsert | CustomModelDataColorsReplaceAll | CustomModelDataColorsReplaceSection


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::CustomModelDataColors": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "values",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "union",
                        "members": [
                            {
                                "kind": "reference",
                                "path": "::java::data::number_provider::NumberProviderRef"
                            },
                            {
                                "kind": "reference",
                                "path": "::java::util::color::RGB"
                            }
                        ]
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

