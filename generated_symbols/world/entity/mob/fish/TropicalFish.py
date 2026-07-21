# Generated from symbols.json for ::java::world::entity::mob::fish::TropicalFish
from dataclasses import dataclass
from generated_symbols.world.entity.mob.fish.Fish import Fish


@dataclass(kw_only=True)
class TropicalFish(Fish):
    Variant: int | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::fish::TropicalFish": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::fish::Fish"
                }
            },
            {
                "kind": "pair",
                "key": "Variant",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}

