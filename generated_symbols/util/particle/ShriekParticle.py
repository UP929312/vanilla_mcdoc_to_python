# Generated from symbols.json for ::java::util::particle::ShriekParticle
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class ShriekParticle:
    delay: Annotated[int, 'Range | Min `0` and above | inclusive']  # Ticks until the particle renders.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::particle::ShriekParticle": {
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
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "key": "value",
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
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "desc": "Ticks until the particle renders.",
                "key": "delay",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                }
            }
        ]
    }
}

