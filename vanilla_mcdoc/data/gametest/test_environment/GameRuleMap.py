"""
Generated from symbols.json for ::java::data::gametest::test_environment::GameRuleMap
Local link to file: vanilla_mcdoc/data/gametest/test_environment/GameRuleMap.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownGameRuleId import KnownGameRuleId


type GameRuleMap = dict[Annotated[str, IdSpec(registry='game_rule')] | KnownGameRuleId, bool | Annotated[int, Field(ge=-1)] | Annotated[int, Field(ge=1)] | Annotated[int, Field(ge=0)] | Annotated[int, Field(ge=1, le=1000)] | Annotated[int, Field(ge=0, le=8)]]
