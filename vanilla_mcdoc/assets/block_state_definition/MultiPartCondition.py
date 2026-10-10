"""
Generated from symbols.json for ::java::assets::block_state_definition::MultiPartCondition
Local link to file: vanilla_mcdoc/assets/block_state_definition/MultiPartCondition.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class MultiPartConditionStruct1(GeneratedModel):
    OR: list[MultiPartCondition]


class MultiPartConditionStruct2(GeneratedModel):
    AND: list[MultiPartCondition]


type MultiPartConditionStruct3 = dict[str, str]


type MultiPartCondition = MultiPartConditionStruct1 | MultiPartConditionStruct2 | MultiPartConditionStruct3


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
                        "key": "AND",
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
