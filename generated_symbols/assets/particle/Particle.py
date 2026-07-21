# Generated from symbols.json for ::java::assets::particle::Particle
from dataclasses import dataclass


@dataclass(kw_only=True)
class Particle:
    textures: list[str]


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

