"""
Generated from symbols.json for ::java::pack::PackBase
Local link to file: generated_symbols/pack/PackBase.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.pack.PackFormat import PackFormat
    from generated_symbols.util.InclusiveRange import InclusiveRange
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class PackBase:
    description: Text
    pack_format: int | None = None  # Optional since 1.21.9. Define it if you want older versions to recognize your pack with a “made for a newer version” warning message.  Because of backwards compatibility, only the main pack format can be used here. Minor formats can only be specified in min and max format.
    supported_formats: InclusiveRange[int] | int | None = None  # Must not be specified in case min_format indicates a format version for 1.21.9 and later.
    min_format: PackFormat | None = None  # The minimun format that is supported. To specify a minor version, use a list of two integers.
    max_format: PackFormat | None = None  # The maximum format that is supported. To specify a minor version, use a list of two integers.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::pack::PackBase": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "description",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::Text"
                }
            },
            {
                "kind": "pair",
                "desc": "Optional since 1.21.9. Define it if you want older versions to recognize your pack with\na \u201cmade for a newer version\u201d warning message.\n\nBecause of backwards compatibility, only the main pack format can\nbe used here. Minor formats can only be specified in min and max format.",
                "key": "pack_format",
                "type": {
                    "kind": "int",
                    "attributes": [
                        {
                            "name": "pack_format"
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
                                "value": "1.20.2"
                            }
                        }
                    }
                ],
                "desc": "Must not be specified in case min_format indicates a format version for 1.21.9 and\nlater.",
                "key": "supported_formats",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::util::InclusiveRange"
                    },
                    "typeArgs": [
                        {
                            "kind": "int",
                            "attributes": [
                                {
                                    "name": "pack_format"
                                }
                            ]
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
                                "value": "1.21.9"
                            }
                        }
                    }
                ],
                "desc": "The minimun format that is supported. To specify a minor version, use a list of two\nintegers.",
                "key": "min_format",
                "type": {
                    "kind": "reference",
                    "path": "::java::pack::PackFormat",
                    "attributes": [
                        {
                            "name": "pack_format"
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
                                "value": "1.21.9"
                            }
                        }
                    }
                ],
                "desc": "The maximum format that is supported. To specify a minor version, use a list of two\nintegers.",
                "key": "max_format",
                "type": {
                    "kind": "reference",
                    "path": "::java::pack::PackFormat",
                    "attributes": [
                        {
                            "name": "pack_format"
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

