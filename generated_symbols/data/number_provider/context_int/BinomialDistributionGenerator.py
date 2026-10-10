"""
Generated from symbols.json for ::java::data::number_provider::context_int::BinomialDistributionGenerator
Local link to file: generated_symbols/data/number_provider/context_int/BinomialDistributionGenerator.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.context_float.FloatRef import FloatRef
    from generated_symbols.data.number_provider.context_int.IntRef import IntRef


class BinomialDistributionGenerator(GeneratedModel):
    n: IntRef  # Number of coin flips.
    p: FloatRef  # Probability of a single coin flip succeeding.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::context_int::BinomialDistributionGenerator": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Number of coin flips.",
                "key": "n",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::context_int::IntRef"
                }
            },
            {
                "kind": "pair",
                "desc": "Probability of a single coin flip succeeding.",
                "key": "p",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::context_float::FloatRef"
                }
            }
        ]
    }
}
