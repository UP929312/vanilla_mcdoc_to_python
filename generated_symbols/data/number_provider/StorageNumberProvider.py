# Generated from symbols.json for ::java::data::number_provider::StorageNumberProvider
from dataclasses import dataclass
from typing import Annotated

from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class StorageNumberProvider:
    storage: Annotated[str, IdSpec(registry='storage')]
    path: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::StorageNumberProvider": {
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

