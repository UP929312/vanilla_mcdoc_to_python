# Generated from symbols.json for ::java::world::entity::mob::breedable::axolotl::Axolotl
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.mob.breedable.Breedable import Breedable

if TYPE_CHECKING:
    from generated_symbols.world.entity.mob.breedable.axolotl.AxolotlVariantInt import AxolotlVariantInt


@dataclass(kw_only=True)
class Axolotl(Breedable):
    Variant: AxolotlVariantInt | None = None  # The variant of the axolotl.
    FromBucket: bool | None = None  # If this axolotl was released from a bucket.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::axolotl::Axolotl": {
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
                "desc": "The variant of the axolotl.",
                "key": "Variant",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::axolotl::AxolotlVariantInt"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "If this axolotl was released from a bucket.",
                "key": "FromBucket",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

