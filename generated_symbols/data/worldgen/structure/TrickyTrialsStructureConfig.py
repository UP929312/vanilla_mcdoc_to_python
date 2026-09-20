"""
Generated from symbols.json for ::java::data::worldgen::structure::TrickyTrialsStructureConfig
Local link to file: generated_symbols/data/worldgen/structure/TrickyTrialsStructureConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.structure.LiquidSettings import LiquidSettings


class DimensionPaddingStruct(GeneratedModel):
    bottom: Annotated[int, Field(ge=0)] | None = None
    top: Annotated[int, Field(ge=0)] | None = None


class TrickyTrialsStructureConfig(GeneratedModel):
    dimension_padding: Annotated[int, Field(ge=0)] | DimensionPaddingStruct | None = None
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

