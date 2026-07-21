# Generated from symbols.json for ::java::world::entity::mob::breedable::tamable::Wolf
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.mob.NeutralMob import NeutralMob
from generated_symbols.world.entity.mob.breedable.tamable.Tamable import Tamable

if TYPE_CHECKING:
    from generated_symbols.util.DyeColorByte import DyeColorByte


@dataclass(kw_only=True)
class Wolf(Tamable, NeutralMob):
    CollarColor: DyeColorByte | None = None  # Collar color, present for wild wolfs. Defaults to 14 (red).
    variant: str | None = None
    sound_variant: str | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::tamable::Wolf": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::tamable::Tamable"
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::NeutralMob"
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
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "desc": "Whether it is angry.",
                "key": "Angry",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Collar color, present for wild wolfs. Defaults to 14 (red).",
                "key": "CollarColor",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::DyeColorByte"
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
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "key": "variant",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "wolf_variant"
                                }
                            }
                        }
                    ]
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
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "key": "sound_variant",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "wolf_sound_variant"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

