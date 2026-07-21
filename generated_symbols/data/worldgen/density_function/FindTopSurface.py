# Generated from symbols.json for ::java::data::worldgen::density_function::FindTopSurface
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef


@dataclass(kw_only=True)
class FindTopSurface:
    density: DensityFunctionRef
    upper_bound: DensityFunctionRef
    lower_bound: Annotated[int, 'Range | `-4064`-`4062` | both inclusive']
    cell_height: Annotated[int, 'Range | Min `1` and above | inclusive']


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

