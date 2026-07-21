# Generated from symbols.json for ::java::util::particle::DustColorTransitionParticle
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.util.particle.DustColor import DustColor


@dataclass(kw_only=True)
class DustColorTransitionParticle:
    from_color: DustColor
    to_color: DustColor
    scale: Annotated[float, 'Range | `0.01`-`4` | both inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::particle::DustColorTransitionParticle": {
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
                            "key": "fromColor",
                            "type": {
                                "kind": "reference",
                                "path": "::java::util::particle::DustColor"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "toColor",
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
                            "key": "from_color",
                            "type": {
                                "kind": "reference",
                                "path": "::java::util::particle::DustColor"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "to_color",
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

