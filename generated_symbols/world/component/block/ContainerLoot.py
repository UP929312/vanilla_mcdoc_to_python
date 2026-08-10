"""
Generated from symbols.json for ::java::world::component::block::ContainerLoot
Local link to file: generated_symbols/world/component/block/ContainerLoot.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class ContainerLoot:
    loot_table: Annotated[str, IdSpec(registry='loot_table')]
    seed: int | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::block::ContainerLoot": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "loot_table",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "loot_table"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "seed",
                "type": {
                    "kind": "long",
                    "attributes": [
                        {
                            "name": "random"
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

