"""
Generated from symbols.json for ::java::assets::block_state_definition::MultiPartCondition
Local link to file: generated_symbols/assets/block_state_definition/MultiPartCondition.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass


@dataclass(kw_only=True)
class MultiPartConditionStruct1:
    OR: list[MultiPartCondition]


type MultiPartConditionStruct2 = dict[str, str]


type MultiPartCondition = MultiPartConditionStruct1 | MultiPartConditionStruct2


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::block_state_definition::MultiPartCondition": {
        "kind": "union",
        "members": [
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "OR",
                        "type": {
                            "kind": "list",
                            "item": {
                                "kind": "reference",
                                "path": "::java::assets::block_state_definition::MultiPartCondition"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": {
                            "kind": "string"
                        },
                        "type": {
                            "kind": "string"
                        }
                    }
                ]
            }
        ]
    }
}

