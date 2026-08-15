"""
Generated from symbols.json for ::java::pack::Pack
Local link to file: generated_symbols/pack/Pack.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.pack.PackFeatures import PackFeatures
    from generated_symbols.pack.PackFilter import PackFilter
    from generated_symbols.pack.PackFormat import PackFormat
    from generated_symbols.pack.PackOverlays import PackOverlays
    from generated_symbols.util.InclusiveRange import InclusiveRange
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class PackStruct:
    description: Text
    pack_format: int | None = None  # Optional since 1.21.9. Define it if you want older versions to recognize your pack with a “made for a newer version” warning message.  Because of backwards compatibility, only the main pack format can be used here. Minor formats can only be specified in min and max format.
    supported_formats: InclusiveRange[int] | int | None = None  # Must not be specified in case min_format indicates a format version for 1.21.9 and later.
    min_format: PackFormat | None = None  # The minimun format that is supported. To specify a minor version, use a list of two integers.
    max_format: PackFormat | None = None  # The maximum format that is supported. To specify a minor version, use a list of two integers.


@dataclass(kw_only=True)
class Pack:
    pack: PackStruct
    filter: PackFilter | None = None
    features: PackFeatures | None = None
    overlays: PackOverlays | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::pack::Pack": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "pack",
                "type": {
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
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "filter",
                "type": {
                    "kind": "reference",
                    "path": "::java::pack::PackFilter"
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
                                "value": "1.19.3"
                            }
                        }
                    }
                ],
                "key": "features",
                "type": {
                    "kind": "reference",
                    "path": "::java::pack::PackFeatures"
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
                "key": "overlays",
                "type": {
                    "kind": "reference",
                    "path": "::java::pack::PackOverlays"
                },
                "optional": True
            }
        ]
    }
}

