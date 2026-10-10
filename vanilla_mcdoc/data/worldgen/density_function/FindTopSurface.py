"""
Generated from symbols.json for ::java::data::worldgen::density_function::FindTopSurface
Local link to file: vanilla_mcdoc/data/worldgen/density_function/FindTopSurface.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef


class FindTopSurface(GeneratedModel):
    density: DensityFunctionRef
    upper_bound: DensityFunctionRef
    lower_bound: Annotated[int, Field(ge=-4064, le=4062)]
    cell_height: Annotated[int, Field(ge=1)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::FindTopSurface": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "density",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            },
            {
                "kind": "pair",
                "key": "upper_bound",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            },
            {
                "kind": "pair",
                "key": "lower_bound",
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
                "key": "cell_height",
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
