# Generated from symbols.json for ::java::assets::font::GlyphProviderType
from enum import Enum


class GlyphProviderType(Enum):
    BITMAP = "bitmap"
    TRUETYPE = "ttf"
    SPACE = "space"
    LEGACYUNICODE = "legacy_unicode"
    UNIHEX = "unihex"
    REFERENCE = "reference"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::font::GlyphProviderType": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "Bitmap",
                "value": "bitmap"
            },
            {
                "identifier": "TrueType",
                "value": "ttf"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "identifier": "Space",
                "value": "space"
            },
            {
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20"
                            }
                        }
                    }
                ],
                "identifier": "LegacyUnicode",
                "value": "legacy_unicode"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20"
                            }
                        }
                    }
                ],
                "identifier": "Unihex",
                "value": "unihex"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20"
                            }
                        }
                    }
                ],
                "identifier": "Reference",
                "value": "reference"
            }
        ]
    }
}

