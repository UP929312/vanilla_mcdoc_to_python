# Generated from symbols.json for ::java::data::advancement::predicate::LightningBoltPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.EntityPredicate import EntityPredicate
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


@dataclass(kw_only=True)
class LightningBoltPredicate:
    blocks_set_on_fire: MinMaxBounds[int] | int | None = None
    entity_struck: EntityPredicate | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::LightningBoltPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "blocks_set_on_fire",
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
            },
            {
                "kind": "pair",
                "key": "entity_struck",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::EntityPredicate"
                },
                "optional": True
            }
        ]
    }
}

