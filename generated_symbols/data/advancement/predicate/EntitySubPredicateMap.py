# Generated from symbols.json for ::java::data::advancement::predicate::EntitySubPredicateMap
from typing import Any


type EntitySubPredicateMap = dict[str, Any]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::EntitySubPredicateMap": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "entity_sub_predicate_type"
                                }
                            }
                        }
                    ]
                },
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                {
                                    "keyword": "key"
                                }
                            ]
                        }
                    ],
                    "registry": "minecraft:entity_sub_predicate"
                }
            }
        ]
    }
}

