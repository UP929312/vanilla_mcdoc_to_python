"""
Generated from symbols.json for ::java::data::worldgen::feature::SeaPickleConfig
Local link to file: generated_symbols/data/worldgen/feature/SeaPickleConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from generated_symbols.base import GeneratedModel
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider


class SeaPickleConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    count: IntProvider[Annotated[int, Field(ge=0, le=256)]] | Annotated[int, Field(ge=0, le=256)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::SeaPickleConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "count",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "concrete",
                            "child": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::UniformInt"
                            },
                            "typeArgs": [
                                {
                                    "kind": "int",
                                    "valueRange": {
                                        "kind": 0,
                                        "min": -10,
                                        "max": 128
                                    }
                                },
                                {
                                    "kind": "int",
                                    "valueRange": {
                                        "kind": 0,
                                        "min": 0,
                                        "max": 128
                                    }
                                }
                            ],
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.17"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "concrete",
                            "child": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::IntProvider"
                            },
                            "typeArgs": [
                                {
                                    "kind": "int",
                                    "valueRange": {
                                        "kind": 0,
                                        "min": 0,
                                        "max": 256
                                    }
                                }
                            ],
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.17"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }
}

