# Generated from symbols.json for ::java::world::entity::mob::breedable::horse::Llama
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated
from generated_symbols.world.entity.mob.breedable.horse.ChestedHorse import ChestedHorse

if TYPE_CHECKING:
    from generated_symbols.world.entity.mob.breedable.horse.LlamaVariantInt import LlamaVariantInt


@dataclass(kw_only=True)
class Llama(ChestedHorse):
    Strength: Annotated[int, 'Range | `1`-`5` | both inclusive'] | None = None  # Determines both the number of items it can carry and how likely it is for wolves to run away.
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

