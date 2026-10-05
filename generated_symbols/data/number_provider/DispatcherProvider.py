"""
Generated from symbols.json for ::java::data::number_provider::DispatcherProvider
Local link to file: generated_symbols/data/number_provider/DispatcherProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Generic, TypeVar

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.predicate.PredicateRef import PredicateRef


T = TypeVar('T')

class CasesStruct(GeneratedModel, Generic[T]):
    condition: PredicateRef
    value: T


class DispatcherProvider(GeneratedModel, Generic[T]):
    cases: list[CasesStruct[T]]  # Each condition is tested in order, the first in the list that passes is used.
    default: T | None = None  # Defaults to constant 0.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::DispatcherProvider": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "desc": "Each condition is tested in order, the first in the list that passes is used.",
                    "key": "cases",
                    "type": {
                        "kind": "list",
                        "item": {
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
                                    "key": "value",
                                    "type": {
                                        "kind": "reference",
                                        "path": "::java::data::number_provider::T"
                                    }
                                }
                            ]
                        }
                    }
                },
                {
                    "kind": "pair",
                    "desc": "Defaults to constant 0.",
                    "key": "default",
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

