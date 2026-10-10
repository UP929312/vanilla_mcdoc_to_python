"""
Generated from symbols.json for ::java::data::number_provider::SingleProvider
Local link to file: generated_symbols/data/number_provider/SingleProvider.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from generated_symbols.base import GeneratedModel


T = TypeVar('T')


class SingleProvider(GeneratedModel, Generic[T]):
    input: T


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::SingleProvider": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "key": "input",
                    "type": {
                        "kind": "reference",
                        "path": "::java::data::number_provider::T"
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
