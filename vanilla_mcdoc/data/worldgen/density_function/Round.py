"""
Generated from symbols.json for ::java::data::worldgen::density_function::Round
Local link to file: generated_symbols/data/worldgen/density_function/Round.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef


class Round(GeneratedModel):
    input: DensityFunctionRef
    multiple: DensityFunctionRef | None = None  # Defaults to constant 1.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::Round": {
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
                "desc": "Defaults to constant 1.",
                "key": "multiple",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                },
                "optional": True
            }
        ]
    }
}
