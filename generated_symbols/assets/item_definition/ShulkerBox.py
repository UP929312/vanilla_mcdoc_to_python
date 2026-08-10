"""
Generated from symbols.json for ::java::assets::item_definition::ShulkerBox
Local link to file: generated_symbols/assets/item_definition/ShulkerBox.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class ShulkerBox:
    texture: Annotated[str, IdSpec(registry='texture', path='entity/shulker/')]
    openness: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::ShulkerBox": {
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
                                            "value": "entity/shulker/"
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
                "key": "openness",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                },
                "optional": True
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
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "desc": "Defaults to `up`.",
                "key": "orientation",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::direction::Direction"
                },
                "optional": True
            }
        ]
    }
}

