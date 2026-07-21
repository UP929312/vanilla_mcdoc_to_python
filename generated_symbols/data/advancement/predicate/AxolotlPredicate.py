# Generated from symbols.json for ::java::data::advancement::predicate::AxolotlPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.component.entity.AxolotlVariant import AxolotlVariant


@dataclass(kw_only=True)
class AxolotlPredicate:
    variant: AxolotlVariant


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::AxolotlPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "variant",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::entity::AxolotlVariant"
                }
            }
        ]
    }
}

