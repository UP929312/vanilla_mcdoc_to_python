# Generated from symbols.json for ::java::data::loot::function::Conditions
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.predicate.PredicateRef import PredicateRef


@dataclass(kw_only=True)
class Conditions:
    condition: PredicateRef | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::Conditions": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "conditions",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::loot::condition::LootCondition"
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "condition",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::predicate::PredicateRef"
                },
                "optional": True
            }
        ]
    }
}

