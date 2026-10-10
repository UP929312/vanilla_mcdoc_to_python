"""
Generated from symbols.json for ::java::world::component::predicate::FireworksPredicate
Local link to file: vanilla_mcdoc/world/component/predicate/FireworksPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds
    from vanilla_mcdoc.world.component.predicate.CollectionPredicate import CollectionPredicate
    from vanilla_mcdoc.world.component.predicate.FireworkExplosionPredicate import FireworkExplosionPredicate


class FireworksPredicate(GeneratedModel):
    explosions: CollectionPredicate[FireworkExplosionPredicate] | None = None
    flight_duration: MinMaxBounds[int] | int | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::predicate::FireworksPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "explosions",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::world::component::predicate::CollectionPredicate"
                    },
                    "typeArgs": [
                        {
                            "kind": "reference",
                            "path": "::java::world::component::predicate::FireworkExplosionPredicate"
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "flight_duration",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::util::MinMaxBounds"
                    },
                    "typeArgs": [
                        {
                            "kind": "int"
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}
