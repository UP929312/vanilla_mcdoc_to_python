# Generated from symbols.json for ::java::pack::PackBase
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.pack.PackFormat import PackFormat
    from generated_symbols.util.InclusiveRange import InclusiveRange
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class PackBase:
    description: Text
    pack_format: int | None = None
    supported_formats: InclusiveRange[int] | int | None = None
    min_format: PackFormat | None = None
    max_format: PackFormat | None = None


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
}

