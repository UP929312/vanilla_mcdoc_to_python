# Generated from symbols.json for ::java::util::particle::TintedLeavesParticle
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.color.RGBA import RGBA


@dataclass(kw_only=True)
class TintedLeavesParticle:
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

