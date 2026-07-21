# Generated from symbols.json for ::java::data::enchantment::effect::ParticlePosition
from dataclasses import dataclass


@dataclass(kw_only=True)
class ParticlePosition:
    type: str
    offset: float | None = None  # Defaults to 0.
    scale: float | None = None  # Defaults to 1.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::ParticlePosition": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "entity_position"
                            }
                        },
                        {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "in_bounding_box"
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Defaults to 0.",
                "key": "offset",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Defaults to 1.",
                "key": "scale",
                "type": {
                    "kind": "float"
                },
                "optional": True
            }
        ]
    }
}

