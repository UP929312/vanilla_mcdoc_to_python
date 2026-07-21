# Generated from symbols.json for ::java::assets::font::UnihexProvider
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.font.UnihexOverrideRange import UnihexOverrideRange


@dataclass(kw_only=True)
class UnihexProvider:
    hex_file: str  # ZIP archive containing one or more *.hex files (files in archive with different extensions are ignored).
    size_overrides: list[UnihexOverrideRange] | None = None  # List of ranges to override the size of.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::font::UnihexProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "ZIP archive containing one or more *.hex files (files in archive with different extensions are ignored).",
                "key": "hex_file",
                "type": {
                    "kind": "string"
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.6"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "List of ranges to override the size of.",
                            "key": "size_overrides",
                            "type": {
                                "kind": "list",
                                "item": {
                                    "kind": "reference",
                                    "path": "::java::assets::font::UnihexOverrideRange"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.6"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "List of ranges to override the size of.",
                            "key": "size_overrides",
                            "type": {
                                "kind": "list",
                                "item": {
                                    "kind": "reference",
                                    "path": "::java::assets::font::UnihexOverrideRange"
                                }
                            },
                            "optional": True
                        }
                    ]
                }
            }
        ]
    }
}

