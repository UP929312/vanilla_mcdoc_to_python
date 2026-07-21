# Generated from symbols.json for ::java::data::advancement::predicate::HorsePredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.component.entity.HorseVariant import HorseVariant


@dataclass(kw_only=True)
class HorsePredicate:
    variant: HorseVariant


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::HorsePredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "variant",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::entity::HorseVariant"
                }
            }
        ]
    }
}

