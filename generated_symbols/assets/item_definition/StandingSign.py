# Generated from symbols.json for ::java::assets::item_definition::StandingSign
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.StandingSignAttachment import StandingSignAttachment
    from generated_symbols.assets.item_definition.WoodType import WoodType


@dataclass(kw_only=True)
class StandingSign:
    wood_type: WoodType
    texture: str | None = None
    attachement: StandingSignAttachment | None = None  # There is an extra "e" in the field name. See MC-307498.  Defaults to `ground`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::StandingSign": {
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
                                            "value": "entity/signs/"
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
                "desc": "There is an extra \"e\" in the field name. See MC-307498. \\\nDefaults to `ground`.",
                "key": "attachement",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::StandingSignAttachment"
                },
                "optional": True
            }
        ]
    }
}

