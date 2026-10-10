"""
Generated from symbols.json for ::java::data::number_provider::legacy::StorageNumberProvider
Local link to file: vanilla_mcdoc/data/number_provider/legacy/StorageNumberProvider.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class StorageNumberProvider(GeneratedModel):
    storage: Annotated[str, IdSpec(registry='storage')]
    path: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::legacy::StorageNumberProvider": {
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
                                            "source"
                                        ]
                                    }
                                ],
                                "registry": "minecraft:storage"
                            }
                        }
                    ]
                }
            }
        ]
    }
}
