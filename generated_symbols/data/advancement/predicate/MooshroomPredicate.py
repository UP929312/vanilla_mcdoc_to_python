# Generated from symbols.json for ::java::data::advancement::predicate::MooshroomPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.component.entity.MooshroomType import MooshroomType


@dataclass(kw_only=True)
class MooshroomPredicate:
    variant: MooshroomType


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::MooshroomPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "variant",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::entity::MooshroomType"
                }
            }
        ]
    }
}

