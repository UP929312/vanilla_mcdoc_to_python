"""
Generated from symbols.json for ::java::data::worldgen::noise_settings::DebugFunctionEntry
Local link to file: generated_symbols/data/worldgen/noise_settings/DebugFunctionEntry.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef


@dataclass(kw_only=True)
class DebugFunctionEntry:
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

