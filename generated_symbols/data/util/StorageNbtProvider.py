# Generated from symbols.json for ::java::data::util::StorageNbtProvider
from dataclasses import dataclass


@dataclass(kw_only=True)
class StorageNbtProvider:
    source: str


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

