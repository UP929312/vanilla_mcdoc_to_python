# Generated from symbols.json for ::java::data::loot::function::ToggleTooltips
from dataclasses import dataclass
from generated_symbols.data.loot.function.Conditions import Conditions


@dataclass(kw_only=True)
class ToggleTooltips(Conditions):
    toggles: dict[str, bool]  # Toggles which tooltips are shown.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::ToggleTooltips": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Toggles which tooltips are shown.",
                "key": "toggles",
                "type": {
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
                                            "value": "1.21.5"
                                        }
                                    }
                                }
                            ],
                            "key": {
                                "kind": "reference",
                                "path": "::java::data::loot::function::ToggleableDataComponent",
                                "attributes": [
                                    {
                                        "name": "id"
                                    }
                                ]
                            },
                            "type": {
                                "kind": "boolean"
                            }
                        },
                        {
                            "kind": "pair",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.5"
                                        }
                                    }
                                }
                            ],
                            "key": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "data_component_type"
                                            }
                                        }
                                    }
                                ]
                            },
                            "type": {
                                "kind": "boolean"
                            }
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

