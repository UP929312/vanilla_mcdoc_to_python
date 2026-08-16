"""
Generated from symbols.json for ::java::data::worldgen::feature::ProbabilityConfig
Local link to file: generated_symbols/data/worldgen/feature/ProbabilityConfig.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated, ClassVar


@dataclass(kw_only=True)
class ProbabilityConfig:
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    probability: Annotated[float, 'Range | `0`-`1` | both inclusive']


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

