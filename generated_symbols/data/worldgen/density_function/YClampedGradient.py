# Generated from symbols.json for ::java::data::worldgen::density_function::YClampedGradient
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.density_function.NoiseRange import NoiseRange


@dataclass(kw_only=True)
class YClampedGradient:
    from_y: Annotated[int, 'Range | `-4064`-`4062` | both inclusive']
    to_y: Annotated[int, 'Range | `-4064`-`4062` | both inclusive']
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

