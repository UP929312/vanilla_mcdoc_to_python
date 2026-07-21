# Generated from symbols.json for ::java::util::particle::SculkChargeParticle
from dataclasses import dataclass


@dataclass(kw_only=True)
class SculkChargeParticle:
    roll: float  # Angle the particle texture is rotated to, measured in radians (π ~ 3.14 for 180° clockwise, negative for counter clockwise).


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::particle::SculkChargeParticle": {
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
                    "kind": "float"
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
                "desc": "Angle the particle texture is rotated to, measured in radians (\u03c0 ~ 3.14 for 180\u00b0 clockwise, negative for counter clockwise).",
                "key": "roll",
                "type": {
                    "kind": "float"
                }
            }
        ]
    }
}

