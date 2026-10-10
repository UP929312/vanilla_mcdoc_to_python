"""
Generated from symbols.json for ::java::util::particle::DragonBreathParticle
Local link to file: generated_symbols/util/particle/DragonBreathParticle.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel


class DragonBreathParticle(GeneratedModel):
    power: float | None = None  # Multiplier of initial velocity. Defaults to 1.0


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::particle::DragonBreathParticle": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.9"
                            }
                        }
                    }
                ],
                "desc": "Multiplier of initial velocity.\nDefaults to 1.0",
                "key": "power",
                "type": {
                    "kind": "float"
                },
                "optional": True
            }
        ]
    }
}
