"""
Generated from symbols.json for ::java::assets::item_definition::Bed
Local link to file: generated_symbols/assets/item_definition/Bed.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.BedPart import BedPart


@dataclass(kw_only=True)
class Bed:
    texture: Annotated[str, IdSpec(registry='texture', path='entity/bed/')]
    part: BedPart


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::Bed": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "texture",
                "type": {
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
                                            "value": "texture"
                                        }
                                    },
                                    "path": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "entity/bed/"
                                        }
                                    }
                                }
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
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "key": "part",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::BedPart"
                }
            }
        ]
    }
}

