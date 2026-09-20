"""
Generated from symbols.json for ::java::util::particle::EntityEffectParticle
Local link to file: generated_symbols/util/particle/EntityEffectParticle.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.util.particle.TranslucentParticle import TranslucentParticle


class EntityEffectParticle(GeneratedModel):
    color: TranslucentParticle


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::particle::EntityEffectParticle": {
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
                            "key": "a",
                            "type": {
                                "kind": "float"
                            }
                        }
                    ]
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
                "key": "color",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::particle::TranslucentParticle"
                }
            }
        ]
    }
}

