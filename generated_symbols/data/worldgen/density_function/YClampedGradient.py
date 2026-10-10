"""
Generated from symbols.json for ::java::data::worldgen::density_function::YClampedGradient
Local link to file: generated_symbols/data/worldgen/density_function/YClampedGradient.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.density_function.NoiseRange import NoiseRange


class YClampedGradient(GeneratedModel):
    from_y: Annotated[int, Field(ge=-4064, le=4062)]
    to_y: Annotated[int, Field(ge=-4064, le=4062)]
    from_value: NoiseRange
    to_value: NoiseRange


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::YClampedGradient": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "from_y",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": -4064,
                        "max": 4062
                    }
                }
            },
            {
                "kind": "pair",
                "key": "to_y",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": -4064,
                        "max": 4062
                    }
                }
            },
            {
                "kind": "pair",
                "key": "from_value",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::NoiseRange"
                }
            },
            {
                "kind": "pair",
                "key": "to_value",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::NoiseRange"
                }
            }
        ]
    }
}

