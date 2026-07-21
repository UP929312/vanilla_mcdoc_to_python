# Generated from symbols.json for ::java::world::component::predicate::FireworkExplosionPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.component.item.FireworkShape import FireworkShape


@dataclass(kw_only=True)
class FireworkExplosionPredicate:
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

