# Generated from symbols.json for ::java::data::worldgen::structure::TrickyTrialsStructureConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Any

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.structure.LiquidSettings import LiquidSettings


@dataclass(kw_only=True)
class TrickyTrialsStructureConfig:
    dimension_padding: Annotated[int, 'Range | Min `0` and above | inclusive'] | Any | None = None
    liquid_settings: LiquidSettings | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure::TrickyTrialsStructureConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "dimension_padding",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": 0
                            }
                        },
                        {
                            "kind": "struct",
                            "fields": [
                                {
                                    "kind": "pair",
                                    "key": "bottom",
                                    "type": {
                                        "kind": "int",
                                        "valueRange": {
                                            "kind": 0,
                                            "min": 0
                                        }
                                    },
                                    "optional": True
                                },
                                {
                                    "kind": "pair",
                                    "key": "top",
                                    "type": {
                                        "kind": "int",
                                        "valueRange": {
                                            "kind": 0,
                                            "min": 0
                                        }
                                    },
                                    "optional": True
                                }
                            ]
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "liquid_settings",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::structure::LiquidSettings"
                },
                "optional": True
            }
        ]
    }
}

