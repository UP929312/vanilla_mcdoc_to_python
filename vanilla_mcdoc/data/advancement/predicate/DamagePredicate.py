"""
Generated from symbols.json for ::java::data::advancement::predicate::DamagePredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/DamagePredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.predicate.DamageSourcePredicate import DamageSourcePredicate
    from vanilla_mcdoc.data.advancement.predicate.EntityPredicate import EntityPredicate
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


class DamagePredicate(GeneratedModel):
    dealt: MinMaxBounds[float] | float | None = None  # Amount of incoming damage before damage reduction.
    taken: MinMaxBounds[float] | float | None = None  # Amount of incoming damage after damage reduction.
    blocked: bool | None = None  # Whether the damage was successfully blocked.
    source_entity: EntityPredicate | None = None  # Source of the damage (eg: a skeleton shooting an arrow or player igniting tnt).
    type: DamageSourcePredicate | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::DamagePredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Amount of incoming damage before damage reduction.",
                "key": "dealt",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::util::MinMaxBounds"
                    },
                    "typeArgs": [
                        {
                            "kind": "float"
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Amount of incoming damage after damage reduction.",
                "key": "taken",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::util::MinMaxBounds"
                    },
                    "typeArgs": [
                        {
                            "kind": "float"
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the damage was successfully blocked.",
                "key": "blocked",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Source of the damage (eg: a skeleton shooting an arrow or player igniting tnt).",
                "key": "source_entity",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::EntityPredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::DamageSourcePredicate"
                },
                "optional": True
            }
        ]
    }
}
