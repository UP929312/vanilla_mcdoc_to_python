# Generated from symbols.json for ::java::assets::equipment::Equipment
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.equipment.Layers import Layers
    from generated_symbols.assets.equipment.TrimOverride import TrimOverride


@dataclass(kw_only=True)
class Equipment:
    layers: Layers  # List of layers for each model layer type.
    trim_overrides: list[TrimOverride] | None = None  # Replaces trim texture based on armor trim.  Only the first entry that matches is applied.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::equipment::Equipment": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "List of layers for each model layer type.",
                "key": "layers",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::equipment::Layers"
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
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "desc": "Replaces trim texture based on armor trim. \\\nOnly the first entry that matches is applied.",
                "key": "trim_overrides",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::assets::equipment::TrimOverride"
                    }
                },
                "optional": True
            }
        ]
    }
}

