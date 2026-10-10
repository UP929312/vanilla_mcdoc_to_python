"""
Generated from symbols.json for ::java::data::worldgen::UniformInt
Local link to file: vanilla_mcdoc/data/worldgen/UniformInt.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


Base = TypeVar('Base')
Spread = TypeVar('Spread')


class UniformInt(GeneratedModel, Generic[Base, Spread]):
    base: Base
    spread: Spread


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::UniformInt": {
        "kind": "template",
        "child": {
            "kind": "union",
            "members": [
                {
                    "kind": "reference",
                    "path": "::java::data::worldgen::Base"
                },
                {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "base",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::Base"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "spread",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::Spread"
                            }
                        }
                    ]
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::data::worldgen::Base"
            },
            {
                "path": "::java::data::worldgen::Spread"
            }
        ]
    }
}
