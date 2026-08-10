"""
Generated from symbols.json for ::java::assets::particle::Particle
Local link to file: generated_symbols/assets/particle/Particle.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class Particle:
    textures: list[Annotated[str, IdSpec(registry='texture', path='particle/')]]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::particle::Particle": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "textures",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string",
                        "attributes": [
                            {
                                "name": "id",
                                "value": {
                                    "kind": "tree",
                                    "values": {
                                        "registry": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "texture"
                                            }
                                        },
                                        "path": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "particle/"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    }
                }
            }
        ]
    }
}

