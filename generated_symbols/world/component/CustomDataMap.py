# Generated from symbols.json for ::java::world::component::CustomDataMap
from typing import Any


type CustomDataMap = dict[str, Any]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::CustomDataMap": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "dispatcher_key",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "mcdoc:custom_data"
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
                    "registry": "mcdoc:custom_data"
                },
                "optional": True
            }
        ]
    }
}

