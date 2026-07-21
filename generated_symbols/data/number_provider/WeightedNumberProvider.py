# Generated from symbols.json for ::java::data::number_provider::WeightedNumberProvider
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.NumberProviderRef import NumberProviderRef
    from generated_symbols.util.NonEmptyWeightedList import NonEmptyWeightedList


@dataclass(kw_only=True)
class WeightedNumberProvider:
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

