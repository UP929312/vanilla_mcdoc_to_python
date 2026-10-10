"""
Generated from symbols.json for ::java::data::number_provider::context_int::ScoreboardValue
Local link to file: vanilla_mcdoc/data/number_provider/context_int/ScoreboardValue.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.context_int.IntRef import IntRef
    from vanilla_mcdoc.data.util.ScoreProvider import ScoreProvider


class ScoreboardValue(GeneratedModel):
    target: ScoreProvider
    score: str
    fallback: IntRef | None = None  # Defaults to constant 0.
