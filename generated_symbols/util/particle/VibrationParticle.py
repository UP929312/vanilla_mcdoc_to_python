# Generated from symbols.json for ::java::util::particle::VibrationParticle
from dataclasses import dataclass
from generated_symbols.util.particle.VibrationParticleData import VibrationParticleData


@dataclass(kw_only=True)
class VibrationParticle(VibrationParticleData):
    pass


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::particle::VibrationParticle": {
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
                    "kind": "reference",
                    "path": "::java::util::particle::VibrationParticleData"
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
                    "kind": "reference",
                    "path": "::java::util::particle::VibrationParticleData"
                }
            }
        ]
    }
}

