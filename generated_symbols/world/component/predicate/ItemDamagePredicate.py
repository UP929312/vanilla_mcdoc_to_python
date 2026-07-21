# Generated from symbols.json for ::java::world::component::predicate::ItemDamagePredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


@dataclass(kw_only=True)
class ItemDamagePredicate:
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

