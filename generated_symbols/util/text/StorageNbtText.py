"""
Generated from symbols.json for ::java::util::text::StorageNbtText
Local link to file: generated_symbols/util/text/StorageNbtText.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated, Literal

from generated_symbols.util.text.TextNbtBase import TextNbtBase
from minecraft_registry import IdSpec


@dataclass(kw_only=True)
class StorageNbtText(TextNbtBase):
    storage: Annotated[str, IdSpec(registry='storage')]
    nbt: str
    source: Literal['storage'] | None = None
    type: Literal['nbt'] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::StorageNbtText": {
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
                "key": "nbt",
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
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20.3"
                            }
                        }
                    }
                ],
                "key": "source",
                "type": {
                    "kind": "literal",
                    "value": {
                        "kind": "string",
                        "value": "storage"
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20.3"
                            }
                        }
                    }
                ],
                "key": "type",
                "type": {
                    "kind": "literal",
                    "value": {
                        "kind": "string",
                        "value": "nbt"
                    }
                },
                "optional": True
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::TextNbtBase"
                }
            }
        ]
    }
}

