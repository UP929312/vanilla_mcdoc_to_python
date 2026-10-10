"""
Generated from symbols.json for ::java::data::number_provider::DistributionProvider
Local link to file: vanilla_mcdoc/data/number_provider/DistributionProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.NonEmptyWeightedList import NonEmptyWeightedList


T = TypeVar('T')


class DistributionProvider(GeneratedModel, Generic[T]):
    distribution: NonEmptyWeightedList[T]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::DistributionProvider": {
        "kind": "template",
        "child": {
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
                                "path": "::java::data::number_provider::T"
                            }
                        ]
                    }
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::data::number_provider::T"
            }
        ]
    }
}
