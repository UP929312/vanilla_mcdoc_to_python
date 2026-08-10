"""
Generated from symbols.json for ::java::data::advancement::AdvancementIcon
Local link to file: generated_symbols/data/advancement/AdvancementIcon.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class AdvancementIcon:
    item: Annotated[str, IdSpec(registry='item')]
    nbt: str | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::AdvancementIcon": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "item",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "item"
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
                            "name": "nbt",
                            "value": {
                                "kind": "dispatcher",
                                "parallelIndices": [
                                    {
                                        "kind": "dynamic",
                                        "accessor": [
                                            "item"
                                        ]
                                    }
                                ],
                                "registry": "minecraft:item"
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

