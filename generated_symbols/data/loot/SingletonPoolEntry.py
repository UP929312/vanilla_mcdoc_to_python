# Generated from symbols.json for ::java::data::loot::SingletonPoolEntry
from dataclasses import dataclass
from typing import Annotated
from generated_symbols.data.loot.LootPoolEntryBase import LootPoolEntryBase


@dataclass(kw_only=True)
class SingletonPoolEntry(LootPoolEntryBase):
    weight: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None
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

