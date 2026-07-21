# Generated from symbols.json for ::java::util::particle::OldDustParticle
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class OldDustParticle:
    r: float
    g: float
    b: float
    scale: Annotated[float, 'Range | `0.01`-`4` | both inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::particle::OldDustParticle": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "r",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "key": "g",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "key": "b",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "key": "scale",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0.01,
                        "max": 4
                    }
                }
            }
        ]
    }
}

