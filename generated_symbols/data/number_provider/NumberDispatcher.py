# Generated from symbols.json for ::java::data::number_provider::NumberDispatcher
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.NumberProviderRef import NumberProviderRef


@dataclass(kw_only=True)
class NumberDispatcher:
    cases: list[Any]
    default: NumberProviderRef | None = None  # Defaults to constant 0.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::NumberDispatcher": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
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
                                "key": "number_provider",
                                "type": {
                                    "kind": "reference",
                                    "path": "::java::data::number_provider::NumberProviderRef"
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
                    "path": "::java::data::number_provider::NumberProviderRef"
                },
                "optional": True
            }
        ]
    }
}

