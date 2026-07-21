# Generated from symbols.json for ::java::data::dialog::body::DialogBody
from dataclasses import dataclass


@dataclass(kw_only=True)
class DialogBody:
    type: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::body::DialogBody": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "dialog_body_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:dialog_body"
                }
            }
        ]
    }
}

