# Generated from symbols.json for ::java::data::advancement::predicate::FoxPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.component.entity.FoxType import FoxType


@dataclass(kw_only=True)
class FoxPredicate:
    variant: FoxType


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::FoxPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "variant",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::entity::FoxType"
                }
            }
        ]
    }
}

