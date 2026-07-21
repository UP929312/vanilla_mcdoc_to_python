# Generated from symbols.json for ::java::util::particle::FlashParticle
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.particle.TranslucentParticle import TranslucentParticle


@dataclass(kw_only=True)
class FlashParticle:
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

