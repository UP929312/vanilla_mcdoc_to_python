"""
Generated from symbols.json for ::java::data::number_provider::context_int::BinomialDistributionGenerator
Local link to file: vanilla_mcdoc/data/number_provider/context_int/BinomialDistributionGenerator.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.context_float.FloatRef import FloatRef
    from vanilla_mcdoc.data.number_provider.context_int.IntRef import IntRef


class BinomialDistributionGenerator(GeneratedModel):
    n: IntRef  # Number of coin flips.
    p: FloatRef  # Probability of a single coin flip succeeding.
