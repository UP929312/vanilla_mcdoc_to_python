"""
Generated from symbols.json for ::java::data::loot::function::SetCustomModelData
Local link to file: generated_symbols/data/loot/function/SetCustomModelData.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.NumberProviderRef import NumberProviderRef
    from generated_symbols.util.color.RGB import RGB


@dataclass(kw_only=True)
class FloatsStructAppend:
    values: list[NumberProviderRef]
    mode: Literal['minecraft:append']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class FloatsStructInsert:
    values: list[NumberProviderRef]
    mode: Literal['minecraft:insert']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset in the list to insert into. Defaults to 0.


@dataclass(kw_only=True)
class FloatsStructReplaceAll:
    values: list[NumberProviderRef]
    mode: Literal['minecraft:replace_all']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class FloatsStructReplaceSection:
    values: list[NumberProviderRef]
    mode: Literal['minecraft:replace_section']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset of the section to replace. Defaults to 0.
    size: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The size of the section to replace. Defaults to size of the new list.


type FloatsStruct = FloatsStructAppend | FloatsStructInsert | FloatsStructReplaceAll | FloatsStructReplaceSection

@dataclass(kw_only=True)
class FlagsStructAppend:
    values: list[bool]
    mode: Literal['minecraft:append']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class FlagsStructInsert:
    values: list[bool]
    mode: Literal['minecraft:insert']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset in the list to insert into. Defaults to 0.


@dataclass(kw_only=True)
class FlagsStructReplaceAll:
    values: list[bool]
    mode: Literal['minecraft:replace_all']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class FlagsStructReplaceSection:
    values: list[bool]
    mode: Literal['minecraft:replace_section']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset of the section to replace. Defaults to 0.
    size: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The size of the section to replace. Defaults to size of the new list.


type FlagsStruct = FlagsStructAppend | FlagsStructInsert | FlagsStructReplaceAll | FlagsStructReplaceSection

@dataclass(kw_only=True)
class StringsStructAppend:
    values: list[str]
    mode: Literal['minecraft:append']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class StringsStructInsert:
    values: list[str]
    mode: Literal['minecraft:insert']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset in the list to insert into. Defaults to 0.


@dataclass(kw_only=True)
class StringsStructReplaceAll:
    values: list[str]
    mode: Literal['minecraft:replace_all']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class StringsStructReplaceSection:
    values: list[str]
    mode: Literal['minecraft:replace_section']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset of the section to replace. Defaults to 0.
    size: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The size of the section to replace. Defaults to size of the new list.


type StringsStruct = StringsStructAppend | StringsStructInsert | StringsStructReplaceAll | StringsStructReplaceSection

@dataclass(kw_only=True)
class ColorsStructAppend:
    values: list[NumberProviderRef | RGB]
    mode: Literal['minecraft:append']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class ColorsStructInsert:
    values: list[NumberProviderRef | RGB]
    mode: Literal['minecraft:insert']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset in the list to insert into. Defaults to 0.


@dataclass(kw_only=True)
class ColorsStructReplaceAll:
    values: list[NumberProviderRef | RGB]
    mode: Literal['minecraft:replace_all']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class ColorsStructReplaceSection:
    values: list[NumberProviderRef | RGB]
    mode: Literal['minecraft:replace_section']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset of the section to replace. Defaults to 0.
    size: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The size of the section to replace. Defaults to size of the new list.


type ColorsStruct = ColorsStructAppend | ColorsStructInsert | ColorsStructReplaceAll | ColorsStructReplaceSection

@dataclass(kw_only=True)
class SetCustomModelData(Conditions):
    floats: FloatsStruct | None = None
    flags: FlagsStruct | None = None
    strings: StringsStruct | None = None
    colors: ColorsStruct | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::SetCustomModelData": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.4"
                            }
                        }
                    }
                ],
                "desc": "Tag that describes the custom model an item will take.\nUsed by the `custom_model_data` model overrides predicate.\nHas certain restrictions due to float conversion.",
                "key": "value",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::NumberProviderRef"
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.4"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "floats",
                            "type": {
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
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "flags",
                            "type": {
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
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "strings",
                            "type": {
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
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "colors",
                            "type": {
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
                            },
                            "optional": True
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::Conditions"
                }
            }
        ]
    }
}

