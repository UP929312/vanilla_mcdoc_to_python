# Generated from symbols.json for ::java::data::advancement::predicate::ParrotPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.component.entity.ParrotVariant import ParrotVariant


@dataclass(kw_only=True)
class ParrotPredicate:
    variant: ParrotVariant


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::ParrotPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "variant",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::entity::ParrotVariant"
                }
            }
        ]
    }
}

