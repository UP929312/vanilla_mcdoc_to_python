"""
Generated from symbols.json for ::java::data::loot::function::ToggleTooltips
Local link to file: generated_symbols/data/loot/function/ToggleTooltips.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from generated_symbols.data.loot.function.Conditions import Conditions
from minecraft_registry import IdSpec


@dataclass(kw_only=True)
class ToggleTooltips(Conditions):
    toggles: dict[Annotated[str, IdSpec(registry='data_component_type')], bool]  # Toggles which tooltips are shown.


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

