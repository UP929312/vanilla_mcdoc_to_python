# Generated from symbols.json for ::java::data::gametest::test_environment::AllOffTestEnvironment
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.gametest.test_environment.TestEnvironment import TestEnvironment


@dataclass(kw_only=True)
class AllOffTestEnvironment:
    definitions: list[TestEnvironment]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::gametest::test_environment::AllOffTestEnvironment": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "definitions",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::gametest::test_environment::TestEnvironment"
                    }
                }
            }
        ]
    }
}

