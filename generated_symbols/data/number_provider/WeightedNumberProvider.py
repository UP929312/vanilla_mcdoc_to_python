"""
Generated from symbols.json for ::java::data::number_provider::WeightedNumberProvider
Local link to file: generated_symbols/data/number_provider/WeightedNumberProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.NumberProviderRef import NumberProviderRef
    from generated_symbols.util.NonEmptyWeightedList import NonEmptyWeightedList


class WeightedNumberProvider(GeneratedModel):
    distribution: NonEmptyWeightedList[NumberProviderRef]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::WeightedNumberProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "distribution",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::util::NonEmptyWeightedList"
                    },
                    "typeArgs": [
                        {
                            "kind": "reference",
                            "path": "::java::data::number_provider::NumberProviderRef"
                        }
                    ]
                }
            }
        ]
    }
}

