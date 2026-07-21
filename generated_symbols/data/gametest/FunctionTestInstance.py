# Generated from symbols.json for ::java::data::gametest::FunctionTestInstance
from dataclasses import dataclass
from generated_symbols.data.gametest.TestData import TestData


@dataclass(kw_only=True)
class FunctionTestInstance(TestData):
    function: str  # Test function (Java code) to run.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::gametest::FunctionTestInstance": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::gametest::TestData"
                }
            },
            {
                "kind": "pair",
                "desc": "Test function (Java code) to run.",
                "key": "function",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "test_function"
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}

