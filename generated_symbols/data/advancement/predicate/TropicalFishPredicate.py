# Generated from symbols.json for ::java::data::advancement::predicate::TropicalFishPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.component.entity.TropicalFishPattern import TropicalFishPattern


@dataclass(kw_only=True)
class TropicalFishPredicate:
    variant: TropicalFishPattern


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::TropicalFishPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "variant",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::entity::TropicalFishPattern"
                }
            }
        ]
    }
}

