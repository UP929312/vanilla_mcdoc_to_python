# Generated from symbols.json for ::java::data::gametest::test_environment::DifficultyTestEnvironment
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.gametest.test_environment.Difficulty import Difficulty


@dataclass(kw_only=True)
class DifficultyTestEnvironment:
    difficulty: Difficulty


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::gametest::test_environment::DifficultyTestEnvironment": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "difficulty",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::gametest::test_environment::Difficulty"
                }
            }
        ]
    }
}

