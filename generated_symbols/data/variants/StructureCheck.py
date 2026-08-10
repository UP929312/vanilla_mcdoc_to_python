"""
Generated from symbols.json for ::java::data::variants::StructureCheck
Local link to file: generated_symbols/data/variants/StructureCheck.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class StructureCheck:
    structures: Annotated[str, IdSpec(registry='worldgen/structure', tags='allowed')] | list[Annotated[str, IdSpec(registry='worldgen/structure')]]  # Checks if the entity is spawning in specific structures.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::variants::StructureCheck": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Checks if the entity is spawning in specific structures.",
                "key": "structures",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "registry": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "worldgen/structure"
                                                }
                                            },
                                            "tags": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "allowed"
                                                }
                                            }
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "list",
                            "item": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "worldgen/structure"
                                            }
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        ]
    }
}

