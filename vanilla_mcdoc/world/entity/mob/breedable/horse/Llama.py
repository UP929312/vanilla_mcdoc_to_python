"""
Generated from symbols.json for ::java::world::entity::mob::breedable::horse::Llama
Local link to file: generated_symbols/world/entity/mob/breedable/horse/Llama.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.world.entity.mob.breedable.horse.ChestedHorse import ChestedHorse

if TYPE_CHECKING:
    from generated_symbols.world.entity.mob.breedable.horse.LlamaVariantInt import LlamaVariantInt


class Llama(ChestedHorse):
    Strength: Annotated[int, Field(ge=1, le=5)] | None = None  # Determines both the number of items it can carry and how likely it is for wolves to run away.
    Variant: LlamaVariantInt | None = None  # The variant of this llama.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::horse::Llama": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::horse::ChestedHorse"
                }
            },
            {
                "kind": "pair",
                "desc": "Determines both the number of items it can carry and how likely it is for wolves to run away.",
                "key": "Strength",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 5
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The variant of this llama.",
                "key": "Variant",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::horse::LlamaVariantInt"
                },
                "optional": True
            }
        ]
    }
}
