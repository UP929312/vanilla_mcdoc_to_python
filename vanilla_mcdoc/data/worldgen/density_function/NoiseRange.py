"""
Generated from symbols.json for ::java::data::worldgen::density_function::NoiseRange
Local link to file: generated_symbols/data/worldgen/density_function/NoiseRange.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field


type NoiseRange = Annotated[float, Field(ge=-1000000, le=1000000)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::NoiseRange": {
        "kind": "float",
        "valueRange": {
            "kind": 0,
            "min": -1000000,
            "max": 1000000
        }
    }
}
