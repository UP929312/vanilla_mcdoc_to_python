# Generated from symbols.json for ::java::data::advancement::predicate::RabbitPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.component.entity.RabbitVariant import RabbitVariant


@dataclass(kw_only=True)
class RabbitPredicate:
    variant: RabbitVariant


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::RabbitPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "variant",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::entity::RabbitVariant"
                }
            }
        ]
    }
}

