# Generated from symbols.json for ::java::world::entity::mob::breedable::panda::Panda
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.mob.breedable.Breedable import Breedable

if TYPE_CHECKING:
    from generated_symbols.world.entity.mob.breedable.panda.Gene import Gene


@dataclass(kw_only=True)
class Panda(Breedable):
    MainGene: Gene | None = None  # Displayed gene. If this gene is recessive and 'HiddenGene' is not the same, the panda will display the 'normal' gene.
    HiddenGene: Gene | None = None  # Hidden gene.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::panda::Panda": {
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
                "desc": "Displayed gene.\nIf this gene is recessive and 'HiddenGene' is not the same, the panda will display the 'normal' gene.",
                "key": "MainGene",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::panda::Gene"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Hidden gene.",
                "key": "HiddenGene",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::panda::Gene"
                },
                "optional": True
            }
        ]
    }
}

