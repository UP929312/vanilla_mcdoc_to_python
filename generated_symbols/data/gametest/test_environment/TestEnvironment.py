# Generated from symbols.json for ::java::data::gametest::test_environment::TestEnvironment
from dataclasses import dataclass


@dataclass(kw_only=True)
class TestEnvironment:
    type: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::gametest::test_environment::TestEnvironment": {
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
                                    "value": "test_environment_definition_type"
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
                    "registry": "minecraft:test_environment_definition"
                }
            }
        ]
    }
}

