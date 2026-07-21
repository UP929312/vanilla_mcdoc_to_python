# Generated from symbols.json for ::java::world::component::predicate::FireworksPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds
    from generated_symbols.world.component.predicate.CollectionPredicate import CollectionPredicate
    from generated_symbols.world.component.predicate.FireworkExplosionPredicate import FireworkExplosionPredicate


@dataclass(kw_only=True)
class FireworksPredicate:
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

