# Generated from symbols.json for ::java::world::entity::mob::breedable::horse::TraderLlama
from dataclasses import dataclass
from generated_symbols.world.entity.mob.breedable.horse.Llama import Llama


@dataclass(kw_only=True)
class TraderLlama(Llama):
    DespawnDelay: int | None = None  # When it will despawn.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::horse::TraderLlama": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::horse::Llama"
                }
            },
            {
                "kind": "pair",
                "desc": "When it will despawn.",
                "key": "DespawnDelay",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}

