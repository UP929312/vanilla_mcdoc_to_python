"""
Generated from symbols.json for ::java::world::entity::mob::fish::TropicalFish
Local link to file: vanilla_mcdoc/world/entity/mob/fish/TropicalFish.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.mob.fish.Fish import Fish


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
