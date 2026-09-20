"""
Generated from symbols.json for ::java::data::gametest::test_environment::DifficultyTestEnvironment
Local link to file: generated_symbols/data/gametest/test_environment/DifficultyTestEnvironment.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.gametest.test_environment.Difficulty import Difficulty


class DifficultyTestEnvironment(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'test_environment'

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

