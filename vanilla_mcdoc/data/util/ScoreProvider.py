"""
Generated from symbols.json for ::java::data::util::ScoreProvider
Local link to file: vanilla_mcdoc/data/util/ScoreProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.data.util.ContextScoreProvider import ContextScoreProvider
from vanilla_mcdoc.data.util.FixedScoreProvider import FixedScoreProvider

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget


class ScoreProviderStructContext(ContextScoreProvider):
    type: Literal['minecraft:context', 'context'] = 'minecraft:context'


class ScoreProviderStructFixed(FixedScoreProvider):
    type: Literal['minecraft:fixed', 'fixed'] = 'minecraft:fixed'


type ScoreProviderStruct = Annotated[
    ScoreProviderStructContext | ScoreProviderStructFixed,
    Field(discriminator='type'),
]


type ScoreProvider = EntityTarget | ScoreProviderStruct
