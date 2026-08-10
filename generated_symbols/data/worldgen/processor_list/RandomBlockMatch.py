"""
Generated from symbols.json for ::java::data::worldgen::processor_list::RandomBlockMatch
Local link to file: generated_symbols/data/worldgen/processor_list/RandomBlockMatch.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class RandomBlockMatch:
    block: Annotated[str, IdSpec(registry='block')]
    probability: Annotated[float, 'Range | `0`-`1` | both inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::RandomBlockMatch": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "block",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "block"
                                }
                            }
                        }
                    ]
                }
            },
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

