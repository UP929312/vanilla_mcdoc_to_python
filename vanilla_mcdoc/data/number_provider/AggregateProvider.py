"""
Generated from symbols.json for ::java::data::number_provider::AggregateProvider
Local link to file: vanilla_mcdoc/data/number_provider/AggregateProvider.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


S = TypeVar('S')


class AggregateProvider(GeneratedModel, Generic[S]):
    inputs: S


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::AggregateProvider": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "key": "inputs",
                    "type": {
                        "kind": "reference",
                        "path": "::java::data::number_provider::S"
                    }
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::data::number_provider::S"
            }
        ]
    }
}
