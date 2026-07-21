# Generated from symbols.json for ::java::util::particle::TrailParticle
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.util.color.RGB import RGB


@dataclass(kw_only=True)
class TrailParticle:
    target: tuple[float, float, float]
    color: RGB
    duration: Annotated[int, 'Range | Min `1` and above | inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::particle::TrailParticle": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "target",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "double"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                }
            },
            {
                "kind": "pair",
                "key": "color",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::color::RGB"
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
                                "value": "1.21.4"
                            }
                        }
                    }
                ],
                "key": "duration",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            }
        ]
    }
}

