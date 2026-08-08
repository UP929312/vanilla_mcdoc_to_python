# Generated from symbols.json for ::java::pack::Pack
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
    pack_format: int | None = None
    supported_formats: InclusiveRange[int] | int | None = None
    min_format: PackFormat | None = None
    max_format: PackFormat | None = None


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

