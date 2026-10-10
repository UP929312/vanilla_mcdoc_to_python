"""
Generated from symbols.json for ::java::data::worldgen::density_function::Interpolated
Local link to file: generated_symbols/data/worldgen/density_function/Interpolated.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.data.worldgen.density_function.OneArgument import OneArgument


class Interpolated(OneArgument):
    cell_size_xz: Annotated[int, Field(ge=1)]
    cell_size_y: Annotated[int, Field(ge=1)]


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
