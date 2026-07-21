# Generated from symbols.json for ::java::world::entity::mob::breedable::mooshroom::Mooshroom
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any
from generated_symbols.world.entity.mob.breedable.Breedable import Breedable

if TYPE_CHECKING:
    from generated_symbols.world.component.entity.MooshroomType import MooshroomType


@dataclass(kw_only=True)
class Mooshroom(Breedable):
    Type: MooshroomType | None = None
    stew_effects: Any | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::mooshroom::Mooshroom": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::Breedable"
                }
            },
            {
                "kind": "pair",
                "key": "Type",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::entity::MooshroomType"
                },
                "optional": True
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
                                "value": "1.20.2"
                            }
                        }
                    }
                ],
                "desc": "Effect that the mooshroom gives to suspicious stew.",
                "key": "EffectId",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::effect::EffectId"
                },
                "optional": True
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
                                "value": "1.20.2"
                            }
                        }
                    }
                ],
                "desc": "Duration of the suspicious stew effect.",
                "key": "EffectDuration",
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
                                "value": "1.20.2"
                            }
                        }
                    }
                ],
                "key": "stew_effects",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "static",
                            "value": "suspicious_stew_effects"
                        }
                    ],
                    "registry": "minecraft:data_component"
                },
                "optional": True
            }
        ]
    }
}

