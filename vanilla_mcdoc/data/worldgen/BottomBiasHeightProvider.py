"""
Generated from symbols.json for ::java::data::worldgen::BottomBiasHeightProvider
Local link to file: generated_symbols/data/worldgen/BottomBiasHeightProvider.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.data.worldgen.UniformHeightProvider import UniformHeightProvider


class BottomBiasHeightProvider(UniformHeightProvider):
    inner: Annotated[int, Field(ge=1)] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::BottomBiasHeightProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::UniformHeightProvider"
                }
            },
            {
                "kind": "pair",
                "key": "inner",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                },
                "optional": True
            }
        ]
    }
}
