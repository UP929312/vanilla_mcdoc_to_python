# Generated from symbols.json for ::java::world::entity::mob::breedable::tamable::Parrot
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.mob.breedable.tamable.Tamable import Tamable

if TYPE_CHECKING:
    from generated_symbols.world.entity.mob.breedable.tamable.ParrotVariantInt import ParrotVariantInt


@dataclass(kw_only=True)
class Parrot(Tamable):
    Variant: ParrotVariantInt | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::tamable::Parrot": {
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
                "key": "Variant",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::tamable::ParrotVariantInt"
                },
                "optional": True
            }
        ]
    }
}

