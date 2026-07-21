# Generated from symbols.json for ::java::world::entity::mob::player::Abilities
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class Abilities:
    walkSpeed: Annotated[float, 'Range | `0.1`-`0.1` | both inclusive'] | None = None  # Speed that the player walks at.
    flySpeed: Annotated[float, 'Range | `0.05`-`0.05` | both inclusive'] | None = None  # Speed that the player flies at.
    mayfly: bool | None = None  # Whether the player can fly.
    flying: bool | None = None  # Whether the player is flying.
    invulnerable: bool | None = None  # Whether the player can only take damage from the void.
    mayBuild: bool | None = None  # Whether the player may build.
    instabuild: bool | None = None  # Whether the player destroys blocks instantly.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::player::Abilities": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Speed that the player walks at.",
                "key": "walkSpeed",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0.1,
                        "max": 0.1
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Speed that the player flies at.",
                "key": "flySpeed",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0.05,
                        "max": 0.05
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the player can fly.",
                "key": "mayfly",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the player is flying.",
                "key": "flying",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the player can only take damage from the void.",
                "key": "invulnerable",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the player may build.",
                "key": "mayBuild",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the player destroys blocks instantly.",
                "key": "instabuild",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

