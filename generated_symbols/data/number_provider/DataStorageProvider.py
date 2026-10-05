"""
Generated from symbols.json for ::java::data::number_provider::DataStorageProvider
Local link to file: generated_symbols/data/number_provider/DataStorageProvider.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Generic, TypeVar

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec


T = TypeVar('T')

class DataStorageProvider(GeneratedModel, Generic[T]):
    storage: Annotated[str, IdSpec(registry='storage')]
    path: str
    fallback: T | None = None  # Defaults to constant 0.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::DataStorageProvider": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "key": "storage",
                    "type": {
                        "kind": "string",
                        "attributes": [
                            {
                                "name": "id",
                                "value": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "storage"
                                    }
                                }
                            }
                        ]
                    }
                },
                {
                    "kind": "pair",
                    "key": "path",
                    "type": {
                        "kind": "string",
                        "attributes": [
                            {
                                "name": "nbt_path",
                                "value": {
                                    "kind": "dispatcher",
                                    "parallelIndices": [
                                        {
                                            "kind": "dynamic",
                                            "accessor": [
                                                "storage"
                                            ]
                                        }
                                    ],
                                    "registry": "minecraft:storage"
                                }
                            }
                        ]
                    }
                },
                {
                    "kind": "pair",
                    "desc": "Defaults to constant 0.",
                    "key": "fallback",
                    "type": {
                        "kind": "reference",
                        "path": "::java::data::number_provider::T"
                    },
                    "optional": True
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

