# Generated from symbols.json for ::java::data::number_provider::ConditionalValueNumberProvider
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.NumberProviderRef import NumberProviderRef
    from generated_symbols.data.predicate.PredicateRef import PredicateRef


@dataclass(kw_only=True)
class ConditionalValueNumberProvider:
    condition: PredicateRef
    on_true: NumberProviderRef
    on_false: NumberProviderRef | None = None  # Defaults to constant 0.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::ConditionalValueNumberProvider": {
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
                    "path": "::java::data::number_provider::NumberProviderRef"
                }
            },
            {
                "kind": "pair",
                "desc": "Defaults to constant 0.",
                "key": "on_False",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::NumberProviderRef"
                },
                "optional": True
            }
        ]
    }
}

