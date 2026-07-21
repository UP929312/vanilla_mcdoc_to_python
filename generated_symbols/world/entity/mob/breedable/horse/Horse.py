# Generated from symbols.json for ::java::world::entity::mob::breedable::horse::Horse
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.mob.breedable.horse.HorseBase import HorseBase

if TYPE_CHECKING:
    from generated_symbols.world.entity.mob.breedable.horse.HorseVariantAndMarkings import HorseVariantAndMarkings


@dataclass(kw_only=True)
class Horse(HorseBase):
    Variant: HorseVariantAndMarkings | None = None  # Variant of the horse. Stored as `baseColor | (markings << 8)`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::horse::Horse": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::horse::HorseBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Variant of the horse. Stored as `baseColor | (markings << 8)`.",
                "key": "Variant",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::horse::HorseVariantAndMarkings"
                },
                "optional": True
            }
        ]
    }
}

