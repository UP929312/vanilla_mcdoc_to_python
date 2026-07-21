# Generated from symbols.json for ::java::util::particle::OldDustTransition
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.util.particle.DustColor import DustColor


@dataclass(kw_only=True)
class OldDustTransition:
    fromColor: DustColor
    toColor: DustColor
    scale: Annotated[float, 'Range | `0.01`-`4` | both inclusive']


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

