"""
Generated from symbols.json for ::java::world::entity::mob::breedable::cow::Cow
Local link to file: generated_symbols/world/entity/mob/breedable/cow/Cow.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from generated_symbols.world.entity.mob.breedable.Breedable import Breedable
from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class Cow(Breedable):
    variant: Annotated[str, IdSpec(registry='cow_variant')] | None = None
    sound_variant: Annotated[str, IdSpec(registry='cow_sound_variant')] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::cow::Cow": {
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
                                    "value": "cow_variant"
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
                                    "value": "cow_sound_variant"
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

