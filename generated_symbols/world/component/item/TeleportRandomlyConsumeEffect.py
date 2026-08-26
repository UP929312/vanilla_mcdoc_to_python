"""
Generated from symbols.json for ::java::world::component::item::TeleportRandomlyConsumeEffect
Local link to file: generated_symbols/world/component/item/TeleportRandomlyConsumeEffect.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class TeleportRandomlyConsumeEffect:
    diameter: Annotated[float, 'Range | Min `1` and above | inclusive'] | None = None  # Defaults to 16.
    directional_particles: bool | None = None  # Whether to show a particle trail into the direction of teleportation.  Defaults to `true`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::TeleportRandomlyConsumeEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Defaults to 16.",
                "key": "diameter",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                },
                "optional": True
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
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "desc": "Whether to show a particle trail into the direction of teleportation. \\\nDefaults to `True`.",
                "key": "directional_particles",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

