"""
Generated from symbols.json for ::java::util::particle::OldDustTransition
Local link to file: generated_symbols/util/particle/OldDustTransition.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.util.particle.DustColor import DustColor


class OldDustTransition(GeneratedModel):
    fromColor: DustColor
    toColor: DustColor
    scale: Annotated[float, Field(ge=0.01, le=4)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::particle::OldDustTransition": {
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
}
