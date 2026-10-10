"""
Generated from symbols.json for ::java::data::number_provider::legacy::ScoreNumberProvider
Local link to file: vanilla_mcdoc/data/number_provider/legacy/ScoreNumberProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.ScoreProvider import ScoreProvider


class ScoreNumberProvider(GeneratedModel):
    target: ScoreProvider
    score: str
    scale: float | None = None
