"""
Generated from symbols.json for ::java::data::loot::function::SetCustomModelData
Local link to file: vanilla_mcdoc/data/loot/function/SetCustomModelData.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.data.loot.function.Conditions import Conditions
from vanilla_mcdoc.data.loot.function.InsertListOperation import InsertListOperation
from vanilla_mcdoc.data.loot.function.ReplaceSectionListOperation import ReplaceSectionListOperation

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.FloatNumberProviderRef import FloatNumberProviderRef
    from vanilla_mcdoc.data.number_provider.IntNumberProviderRef import IntNumberProviderRef
    from vanilla_mcdoc.util.color.RGB import RGB


class FloatsStructAppend(GeneratedModel):
    values: list[FloatNumberProviderRef]
    mode: Literal['minecraft:append', 'append'] = 'minecraft:append'  # Determines how the existing list should be modified.


class FloatsStructInsert(InsertListOperation):
    values: list[FloatNumberProviderRef]
    mode: Literal['minecraft:insert', 'insert'] = 'minecraft:insert'  # Determines how the existing list should be modified.


class FloatsStructReplaceAll(GeneratedModel):
    values: list[FloatNumberProviderRef]
    mode: Literal['minecraft:replace_all', 'replace_all'] = 'minecraft:replace_all'  # Determines how the existing list should be modified.


class FloatsStructReplaceSection(ReplaceSectionListOperation):
    values: list[FloatNumberProviderRef]
    mode: Literal['minecraft:replace_section', 'replace_section'] = 'minecraft:replace_section'  # Determines how the existing list should be modified.


type FloatsStruct = Annotated[
    FloatsStructAppend | FloatsStructInsert | FloatsStructReplaceAll | FloatsStructReplaceSection,
    Field(discriminator='mode'),
]


class FlagsStructAppend(GeneratedModel):
    values: list[bool]
    mode: Literal['minecraft:append', 'append'] = 'minecraft:append'  # Determines how the existing list should be modified.


class FlagsStructInsert(InsertListOperation):
    values: list[bool]
    mode: Literal['minecraft:insert', 'insert'] = 'minecraft:insert'  # Determines how the existing list should be modified.


class FlagsStructReplaceAll(GeneratedModel):
    values: list[bool]
    mode: Literal['minecraft:replace_all', 'replace_all'] = 'minecraft:replace_all'  # Determines how the existing list should be modified.


class FlagsStructReplaceSection(ReplaceSectionListOperation):
    values: list[bool]
    mode: Literal['minecraft:replace_section', 'replace_section'] = 'minecraft:replace_section'  # Determines how the existing list should be modified.


type FlagsStruct = Annotated[
    FlagsStructAppend | FlagsStructInsert | FlagsStructReplaceAll | FlagsStructReplaceSection,
    Field(discriminator='mode'),
]


class StringsStructAppend(GeneratedModel):
    values: list[str]
    mode: Literal['minecraft:append', 'append'] = 'minecraft:append'  # Determines how the existing list should be modified.


class StringsStructInsert(InsertListOperation):
    values: list[str]
    mode: Literal['minecraft:insert', 'insert'] = 'minecraft:insert'  # Determines how the existing list should be modified.


class StringsStructReplaceAll(GeneratedModel):
    values: list[str]
    mode: Literal['minecraft:replace_all', 'replace_all'] = 'minecraft:replace_all'  # Determines how the existing list should be modified.


class StringsStructReplaceSection(ReplaceSectionListOperation):
    values: list[str]
    mode: Literal['minecraft:replace_section', 'replace_section'] = 'minecraft:replace_section'  # Determines how the existing list should be modified.


type StringsStruct = Annotated[
    StringsStructAppend | StringsStructInsert | StringsStructReplaceAll | StringsStructReplaceSection,
    Field(discriminator='mode'),
]


class ColorsStructAppend(GeneratedModel):
    values: list[RGB | IntNumberProviderRef]
    mode: Literal['minecraft:append', 'append'] = 'minecraft:append'  # Determines how the existing list should be modified.


class ColorsStructInsert(InsertListOperation):
    values: list[RGB | IntNumberProviderRef]
    mode: Literal['minecraft:insert', 'insert'] = 'minecraft:insert'  # Determines how the existing list should be modified.


class ColorsStructReplaceAll(GeneratedModel):
    values: list[RGB | IntNumberProviderRef]
    mode: Literal['minecraft:replace_all', 'replace_all'] = 'minecraft:replace_all'  # Determines how the existing list should be modified.


class ColorsStructReplaceSection(ReplaceSectionListOperation):
    values: list[RGB | IntNumberProviderRef]
    mode: Literal['minecraft:replace_section', 'replace_section'] = 'minecraft:replace_section'  # Determines how the existing list should be modified.


type ColorsStruct = Annotated[
    ColorsStructAppend | ColorsStructInsert | ColorsStructReplaceAll | ColorsStructReplaceSection,
    Field(discriminator='mode'),
]


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
                    "path": "::java::data::number_provider::LegacyNumberProvider"
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
                                                "path": "::java::data::number_provider::FloatNumberProviderRef"
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
                                                        "path": "::java::util::color::RGB"
                                                    },
                                                    {
                                                        "kind": "reference",
                                                        "path": "::java::data::number_provider::IntNumberProviderRef"
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
