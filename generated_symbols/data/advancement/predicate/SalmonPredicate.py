# Generated from symbols.json for ::java::data::advancement::predicate::SalmonPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.SalmonVariant import SalmonVariant


@dataclass(kw_only=True)
class SalmonPredicate:
    variant: SalmonVariant | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::SalmonPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "variant",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::SalmonVariant"
                },
                "optional": True
            }
        ]
    }
}

