# Generated from symbols.json for ::java::util::particle::GeyserParticle
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class GeyserParticle:
    water_blocks: Annotated[int, 'Range | Min `1` and above | inclusive']  # Scales the particle size and its burst impulse.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::particle::GeyserParticle": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Scales the particle size and its burst impulse.",
                "key": "water_blocks",
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

