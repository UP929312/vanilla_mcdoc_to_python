# Generated from symbols.json for ::java::data::advancement::predicate::LlamaPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.component.entity.LlamaVariant import LlamaVariant


@dataclass(kw_only=True)
class LlamaPredicate:
    variant: LlamaVariant


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::LlamaPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "variant",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::entity::LlamaVariant"
                }
            }
        ]
    }
}

