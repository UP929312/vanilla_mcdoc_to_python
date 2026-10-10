"""
Generated from symbols.json for ::java::data::loot::SingletonPoolEntry
Local link to file: vanilla_mcdoc/data/loot/SingletonPoolEntry.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.data.loot.LootPoolEntryBase import LootPoolEntryBase


class SingletonPoolEntry(LootPoolEntryBase):
    weight: Annotated[int, Field(ge=1)] | None = None
    quality: int | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::SingletonPoolEntry": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "weight",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "quality",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::LootPoolEntryBase"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "functions",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::loot::LootFunction"
                    }
                },
                "optional": True
            }
        ]
    }
}
