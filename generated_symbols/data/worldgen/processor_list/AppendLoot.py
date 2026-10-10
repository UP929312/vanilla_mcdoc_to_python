"""
Generated from symbols.json for ::java::data::worldgen::processor_list::AppendLoot
Local link to file: generated_symbols/data/worldgen/processor_list/AppendLoot.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec


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
