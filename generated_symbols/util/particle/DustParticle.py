# Generated from symbols.json for ::java::util::particle::DustParticle
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.util.particle.DustColor import DustColor


@dataclass(kw_only=True)
class DustParticle:
    color: DustColor
    scale: Annotated[float, 'Range | `0.01`-`4` | both inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::particle::DustParticle": {
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
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "color",
                            "type": {
                                "kind": "reference",
                                "path": "::java::util::particle::DustColor"
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
        ]
    }
}

