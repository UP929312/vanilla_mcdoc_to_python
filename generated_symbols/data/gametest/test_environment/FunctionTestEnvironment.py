# Generated from symbols.json for ::java::data::gametest::test_environment::FunctionTestEnvironment
from dataclasses import dataclass


@dataclass(kw_only=True)
class FunctionTestEnvironment:
    setup: str | None = None
    teardown: str | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::gametest::test_environment::FunctionTestEnvironment": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "setup",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "function"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "teardown",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "function"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

