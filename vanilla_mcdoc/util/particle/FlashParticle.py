"""
Generated from symbols.json for ::java::util::particle::FlashParticle
Local link to file: vanilla_mcdoc/util/particle/FlashParticle.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.particle.TranslucentParticle import TranslucentParticle


class FlashParticle(GeneratedModel):
    color: TranslucentParticle


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::particle::FlashParticle": {
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
                "key": "color",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::particle::TranslucentParticle"
                }
            }
        ]
    }
}
