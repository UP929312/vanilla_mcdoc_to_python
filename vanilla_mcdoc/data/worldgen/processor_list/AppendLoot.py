"""
Generated from symbols.json for ::java::data::worldgen::processor_list::AppendLoot
Local link to file: vanilla_mcdoc/data/worldgen/processor_list/AppendLoot.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class AppendLoot(GeneratedModel):
    loot_table: Annotated[str, IdSpec(registry='loot_table')]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::AppendLoot": {
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
            }
        ]
    }
}
