"""
Generated from symbols.json for ::java::data::number_provider::ConditionalProvider
Local link to file: generated_symbols/data/number_provider/ConditionalProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Generic, TypeVar

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.predicate.PredicateRef import PredicateRef


T = TypeVar('T')

class ConditionalProvider(GeneratedModel, Generic[T]):
    condition: PredicateRef
    on_true: T
    on_false: T | None = None  # Defaults to constant 0.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::ConditionalProvider": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "key": "condition",
                    "type": {
                        "kind": "reference",
                        "path": "::java::data::predicate::PredicateRef"
                    }
                },
                {
                    "kind": "pair",
                    "key": "on_True",
                    "type": {
                        "kind": "reference",
                        "path": "::java::data::number_provider::T"
                    }
                },
                {
                    "kind": "pair",
                    "desc": "Defaults to constant 0.",
                    "key": "on_False",
                    "type": {
                        "kind": "reference",
                        "path": "::java::data::number_provider::T"
                    },
                    "optional": True
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::data::number_provider::T"
            }
        ]
    }
}

