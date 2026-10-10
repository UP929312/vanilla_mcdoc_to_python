"""
Generated from symbols.json for ::java::data::util::StorageNbtProvider
Local link to file: generated_symbols/data/util/StorageNbtProvider.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec


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
