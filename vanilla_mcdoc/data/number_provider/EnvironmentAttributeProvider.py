"""
Generated from symbols.json for ::java::data::number_provider::EnvironmentAttributeProvider
Local link to file: generated_symbols/data/number_provider/EnvironmentAttributeProvider.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from generated_symbols.base import GeneratedModel


A = TypeVar('A')


class EnvironmentAttributeProvider(GeneratedModel, Generic[A]):
    attribute: A


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::EnvironmentAttributeProvider": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "key": "attribute",
                    "type": {
                        "kind": "reference",
                        "path": "::java::data::number_provider::A"
                    }
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::data::number_provider::A"
            }
        ]
    }
}
