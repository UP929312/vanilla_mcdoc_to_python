# Generated from symbols.json for ::java::data::advancement::predicate::PostComponentsItemPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds
    from generated_symbols.world.component.DataComponentExactPredicate import DataComponentExactPredicate
    from generated_symbols.world.component.DataComponentPredicate import DataComponentPredicate


@dataclass(kw_only=True)
class PostComponentsItemPredicate:
    items: str | list[str] | None = None
    count: MinMaxBounds[int] | int | None = None
    components: DataComponentExactPredicate | None = None
    predicates: DataComponentPredicate | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::PostComponentsItemPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "items",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "registry": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "item"
                                                }
                                            },
                                            "tags": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "allowed"
                                                }
                                            }
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "list",
                            "item": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "item"
                                            }
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "count",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::util::MinMaxBounds"
                    },
                    "typeArgs": [
                        {
                            "kind": "int"
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "components",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::DataComponentExactPredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "predicates",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::DataComponentPredicate"
                },
                "optional": True
            }
        ],
        "attributes": [
            {
                "name": "since",
                "value": {
                    "kind": "literal",
                    "value": {
                        "kind": "string",
                        "value": "1.20.5"
                    }
                }
            }
        ]
    }
}

