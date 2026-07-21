# Generated from symbols.json for ::java::world::component::item::AdventureModePredicate
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.BlockPredicate import BlockPredicate


type AdventureModePredicate = Annotated[list[BlockPredicate], 'Length = 1 (inclusive) and above'] | BlockPredicate


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::AdventureModePredicate": {
        "kind": "union",
        "members": [
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "predicates",
                        "type": {
                            "kind": "list",
                            "item": {
                                "kind": "reference",
                                "path": "::java::data::advancement::predicate::BlockPredicate"
                            },
                            "lengthRange": {
                                "kind": 0,
                                "min": 1
                            }
                        }
                    },
                    {
                        "kind": "pair",
                        "key": "show_in_tooltip",
                        "type": {
                            "kind": "boolean"
                        },
                        "optional": True
                    }
                ],
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    },
                    {
                        "name": "canonical"
                    }
                ]
            },
            {
                "kind": "list",
                "item": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::BlockPredicate"
                },
                "lengthRange": {
                    "kind": 0,
                    "min": 1
                },
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "reference",
                "path": "::java::data::advancement::predicate::BlockPredicate"
            }
        ]
    }
}

