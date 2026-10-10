"""
Generated from symbols.json for ::java::world::component::predicate::ItemDamagePredicate
Local link to file: generated_symbols/world/component/predicate/ItemDamagePredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


class ItemDamagePredicate(GeneratedModel):
    damage: MinMaxBounds[int] | int | None = None
    durability: MinMaxBounds[int] | int | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::predicate::ItemDamagePredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "damage",
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
                "key": "durability",
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
