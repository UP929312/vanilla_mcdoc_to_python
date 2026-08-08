# Generated from symbols.json for ::java::data::loot::function::SetCustomModelData
from dataclasses import dataclass
from typing import TYPE_CHECKING

from generated_symbols.data.loot.function.Conditions import Conditions
from generated_symbols.data.loot.function.ListOperation import ListOperation

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.NumberProviderRef import NumberProviderRef
    from generated_symbols.util.color.RGB import RGB


@dataclass(kw_only=True)
class FloatsStruct(ListOperation):
    values: list[NumberProviderRef]


@dataclass(kw_only=True)
class FlagsStruct(ListOperation):
    values: list[bool]


@dataclass(kw_only=True)
class StringsStruct(ListOperation):
    values: list[str]


@dataclass(kw_only=True)
class ColorsStruct(ListOperation):
    values: list[NumberProviderRef | RGB]


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

