"""
Generated from symbols.json for ::java::data::worldgen::density_function::Shift
Local link to file: generated_symbols/data/worldgen/density_function/Shift.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.density_function.NoiseParametersRef import NoiseParametersRef


@dataclass(kw_only=True)
class Shift:
    noise: NoiseParametersRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::Shift": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "argument",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::NoiseParametersRef"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "noise",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::NoiseParametersRef"
                }
            }
        ]
    }
}

