"""
Generated from symbols.json for ::java::data::worldgen::feature::ProbabilityConfig
Local link to file: generated_symbols/data/worldgen/feature/ProbabilityConfig.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar

from pydantic import Field

from generated_symbols.base import GeneratedModel


class ProbabilityConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    probability: Annotated[float, Field(ge=0, le=1)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::ProbabilityConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "probability",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            }
        ]
    }
}
