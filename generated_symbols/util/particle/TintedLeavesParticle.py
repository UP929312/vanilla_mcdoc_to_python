"""
Generated from symbols.json for ::java::util::particle::TintedLeavesParticle
Local link to file: generated_symbols/util/particle/TintedLeavesParticle.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.util.color.RGBA import RGBA


class TintedLeavesParticle(GeneratedModel):
    color: RGBA


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::particle::TintedLeavesParticle": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "color",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::color::RGBA"
                }
            }
        ]
    }
}

