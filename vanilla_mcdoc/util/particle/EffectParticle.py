"""
Generated from symbols.json for ::java::util::particle::EffectParticle
Local link to file: vanilla_mcdoc/util/particle/EffectParticle.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.color.RGB import RGB


class EffectParticle(GeneratedModel):
    power: float | None = None  # Multiplier of initial velocity. Defaults to 1.0
    color: RGB | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::particle::EffectParticle": {
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
                                "value": "1.21.9"
                            }
                        }
                    }
                ],
                "key": "color",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::color::RGB"
                },
                "optional": True
            }
        ]
    }
}
