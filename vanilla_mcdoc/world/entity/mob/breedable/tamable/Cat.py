"""
Generated from symbols.json for ::java::world::entity::mob::breedable::tamable::Cat
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/tamable/Cat.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.world.entity.mob.breedable.tamable.Tamable import Tamable

if TYPE_CHECKING:
    from vanilla_mcdoc.util.DyeColorByte import DyeColorByte


class Cat(Tamable):
    CollarColor: DyeColorByte | None = None  # Collar color, present for stray cats. Defaults to 14 (red).
    variant: Annotated[str, IdSpec(registry='cat_variant')] | None = None
    sound_variant: Annotated[str, IdSpec(registry='cat_sound_variant')] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::tamable::Cat": {
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
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "CatType",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::tamable::CatType"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Collar color, present for stray cats. Defaults to 14 (red).",
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
                                "value": "1.19"
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
                                    "value": "cat_variant"
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
                                "value": "26.1"
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
                                    "value": "cat_sound_variant"
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
