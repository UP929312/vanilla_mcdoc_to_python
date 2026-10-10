"""
Generated from symbols.json for ::java::data::gametest::test_environment::DifficultyTestEnvironment
Local link to file: vanilla_mcdoc/data/gametest/test_environment/DifficultyTestEnvironment.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.gametest.test_environment.Difficulty import Difficulty


class DifficultyTestEnvironment(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'test_environment'

    difficulty: Difficulty
