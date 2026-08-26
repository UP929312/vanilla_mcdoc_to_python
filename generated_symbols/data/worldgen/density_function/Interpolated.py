"""
Generated from symbols.json for ::java::data::worldgen::density_function::Interpolated
Local link to file: generated_symbols/data/worldgen/density_function/Interpolated.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from generated_symbols.data.worldgen.density_function.OneArgument import OneArgument


@dataclass(kw_only=True)
class Interpolated(OneArgument):
    cell_size_xz: Annotated[int, 'Range | Min `1` and above | inclusive']
    cell_size_y: Annotated[int, 'Range | Min `1` and above | inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::Interpolated": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::OneArgument"
                }
            },
            {
                "kind": "spread",
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
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "cell_size_xz",
                            "type": {
                                "kind": "int",
                                "valueRange": {
                                    "kind": 0,
                                    "min": 1
                                }
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "cell_size_y",
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
        ]
    }
}

