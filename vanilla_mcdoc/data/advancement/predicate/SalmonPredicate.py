"""
Generated from symbols.json for ::java::data::advancement::predicate::SalmonPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/SalmonPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.predicate.SalmonVariant import SalmonVariant


class SalmonPredicate(GeneratedModel):
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
