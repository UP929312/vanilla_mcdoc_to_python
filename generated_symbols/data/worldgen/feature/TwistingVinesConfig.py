"""
Generated from symbols.json for ::java::data::worldgen::feature::TwistingVinesConfig
Local link to file: generated_symbols/data/worldgen/feature/TwistingVinesConfig.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar

from pydantic import Field

from generated_symbols.base import GeneratedModel


class TwistingVinesConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    spread_width: Annotated[int, Field(ge=1)]
    spread_height: Annotated[int, Field(ge=1)]
    max_height: Annotated[int, Field(ge=1)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::TwistingVinesConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "spread_width",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            },
            {
                "kind": "pair",
                "key": "spread_height",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            },
            {
                "kind": "pair",
                "key": "max_height",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            }
        ]
    }
}

