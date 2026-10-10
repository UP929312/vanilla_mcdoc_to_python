"""
Generated from symbols.json for ::java::world::entity::minecart::TntMinecart
Local link to file: generated_symbols/world/entity/minecart/TntMinecart.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.world.entity.minecart.Minecart import Minecart


class TntMinecart(Minecart):
    fuse: int | None = None  # Ticks until it explodes.
    explosion_power: Annotated[float, Field(ge=0, le=128)] | None = None
    explosion_speed_factor: Annotated[float, Field(ge=0, le=128)] | None = None  # Controls the amount of added damage depending on the speed of the minecart.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::minecart::TntMinecart": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::minecart::Minecart"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.4"
                            }
                        }
                    }
                ],
                "desc": "Ticks until it explodes.",
                "key": "TNTFuse",
                "type": {
                    "kind": "int"
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
                                "value": "1.21.4"
                            }
                        }
                    }
                ],
                "desc": "Ticks until it explodes.",
                "key": "fuse",
                "type": {
                    "kind": "int"
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
                                "value": "1.21.2"
                            }
                        }
                    }
                ],
                "key": "explosion_power",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 128
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
                                "value": "1.21.4"
                            }
                        }
                    }
                ],
                "desc": "Controls the amount of added damage depending on the speed of the minecart.",
                "key": "explosion_speed_factor",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 128
                    }
                },
                "optional": True
            }
        ]
    }
}
