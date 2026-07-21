# Generated from symbols.json for ::java::assets::item_definition::HangingSign
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.HangingSignAttachment import HangingSignAttachment
    from generated_symbols.assets.item_definition.WoodType import WoodType


@dataclass(kw_only=True)
class HangingSign:
    wood_type: WoodType
    texture: str | None = None
    attachment: HangingSignAttachment | None = None  # Defaults to `ceiling_middle`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::HangingSign": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "wood_type",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::WoodType"
                }
            },
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
                                            "value": "entity/signs/hanging/"
                                        }
                                    }
                                }
                            }
                        }
                    ]
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
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "desc": "Defaults to `ceiling_middle`.",
                "key": "attachment",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::HangingSignAttachment"
                },
                "optional": True
            }
        ]
    }
}

