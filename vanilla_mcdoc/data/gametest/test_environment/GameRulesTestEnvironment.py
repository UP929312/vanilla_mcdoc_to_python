"""
Generated from symbols.json for ::java::data::gametest::test_environment::GameRulesTestEnvironment
Local link to file: vanilla_mcdoc/data/gametest/test_environment/GameRulesTestEnvironment.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownGameRuleId import KnownGameRuleId


class GameRulesTestEnvironment(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'test_environment'

    rules: dict[Annotated[str, IdSpec(registry='game_rule')] | KnownGameRuleId, bool | Annotated[int, Field(ge=-1)] | Annotated[int, Field(ge=1)] | Annotated[int, Field(ge=0)] | Annotated[int, Field(ge=1, le=1000)] | Annotated[int, Field(ge=0, le=8)]]
