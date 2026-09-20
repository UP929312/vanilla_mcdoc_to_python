"""
Generated from symbols.json for ::java::data::gametest::test_environment::AllOffTestEnvironment
Local link to file: generated_symbols/data/gametest/test_environment/AllOffTestEnvironment.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.gametest.test_environment.TestEnvironment import TestEnvironment


class AllOffTestEnvironment(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'test_environment'

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

