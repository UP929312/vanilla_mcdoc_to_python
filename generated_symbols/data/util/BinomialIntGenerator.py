# Generated from symbols.json for ::java::data::util::BinomialIntGenerator
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class BinomialIntGenerator:
    n: Annotated[int, 'Range | Min `0` and above | inclusive']
    p: Annotated[float, 'Range | `0`-`1` | both inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::util::BinomialIntGenerator": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "n",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                }
            },
            {
                "kind": "pair",
                "key": "p",
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

