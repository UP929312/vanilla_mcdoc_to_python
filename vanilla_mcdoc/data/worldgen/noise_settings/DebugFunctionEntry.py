"""
Generated from symbols.json for ::java::data::worldgen::noise_settings::DebugFunctionEntry
Local link to file: vanilla_mcdoc/data/worldgen/noise_settings/DebugFunctionEntry.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef


class DebugFunctionEntry(GeneratedModel):
    label: str
    function: DensityFunctionRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::noise_settings::DebugFunctionEntry": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "label",
                "type": {
                    "kind": "string"
                }
            },
            {
                "kind": "pair",
                "key": "function",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            }
        ]
    }
}
