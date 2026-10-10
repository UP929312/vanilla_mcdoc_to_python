"""
Generated from symbols.json for ::java::data::util::StorageNbtProvider
Local link to file: vanilla_mcdoc/data/util/StorageNbtProvider.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class StorageNbtProvider(GeneratedModel):
    source: Annotated[str, IdSpec(registry='storage')]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::util::StorageNbtProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "source",
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
            }
        ]
    }
}
