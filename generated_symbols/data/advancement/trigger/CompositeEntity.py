# Generated from symbols.json for ::java::data::advancement::trigger::CompositeEntity
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.advancement.trigger.AdvancementPredicateRef import AdvancementPredicateRef


type CompositeEntity = AdvancementPredicateRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::CompositeEntity": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::data::advancement::predicate::EntityPredicate",
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
                ]
            },
            {
                "kind": "reference",
                "path": "::java::data::advancement::trigger::AdvancementPredicateRef",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.16"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

