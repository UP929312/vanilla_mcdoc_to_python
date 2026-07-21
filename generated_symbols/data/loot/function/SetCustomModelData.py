# Generated from symbols.json for ::java::data::loot::function::SetCustomModelData
from dataclasses import dataclass
from typing import Any
from generated_symbols.data.loot.function.Conditions import Conditions


@dataclass(kw_only=True)
class SetCustomModelData(Conditions):
    floats: Any | None = None
    flags: Any | None = None
    strings: Any | None = None
    colors: Any | None = None


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

