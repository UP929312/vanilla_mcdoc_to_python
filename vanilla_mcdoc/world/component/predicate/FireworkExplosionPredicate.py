"""
Generated from symbols.json for ::java::world::component::predicate::FireworkExplosionPredicate
Local link to file: vanilla_mcdoc/world/component/predicate/FireworkExplosionPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.item.FireworkShape import FireworkShape


class FireworkExplosionPredicate(GeneratedModel):
    shape: FireworkShape | None = None
    has_twinkle: bool | None = None
    has_trail: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::predicate::FireworkExplosionPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "shape",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::item::FireworkShape"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "has_twinkle",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "has_trail",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}
