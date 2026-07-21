# Generated from symbols.json for ::java::data::dialog::action::ClickAction
from dataclasses import dataclass


@dataclass(kw_only=True)
class ClickAction:
    type: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::action::ClickAction": {
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
                                    "value": "dialog_action_type"
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
                    "registry": "minecraft:dialog_action"
                }
            }
        ]
    }
}

