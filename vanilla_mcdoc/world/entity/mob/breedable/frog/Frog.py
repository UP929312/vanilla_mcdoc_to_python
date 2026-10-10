"""
Generated from symbols.json for ::java::world::entity::mob::breedable::frog::Frog
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/frog/Frog.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.world.entity.mob.breedable.Breedable import Breedable


class Frog(Breedable):
    variant: Annotated[str, IdSpec(registry='frog_variant')] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::frog::Frog": {
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
                                    "value": "frog_variant"
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
