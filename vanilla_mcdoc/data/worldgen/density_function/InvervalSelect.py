"""
Generated from symbols.json for ::java::data::worldgen::density_function::InvervalSelect
Local link to file: generated_symbols/data/worldgen/density_function/InvervalSelect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef
    from generated_symbols.data.worldgen.density_function.NoiseRange import NoiseRange


class InvervalSelect(GeneratedModel):
    input: DensityFunctionRef
    thresholds: Annotated[list[NoiseRange], Field(min_length=1)]  # Must have exactly one fewer element than `functions`.
    functions: Annotated[list[DensityFunctionRef], Field(min_length=2)]  # Must have exactly one more element than `thresholds`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::InvervalSelect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "input",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            },
            {
                "kind": "pair",
                "desc": "Must have exactly one fewer element than `functions`.",
                "key": "thresholds",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::density_function::NoiseRange"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "Must have exactly one more element than `thresholds`.",
                "key": "functions",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 2
                    }
                }
            }
        ]
    }
}
