# Generated from symbols.json for ::java::pack::PackOverlay
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.pack.PackFormat import PackFormat
    from generated_symbols.util.InclusiveRange import InclusiveRange


@dataclass(kw_only=True)
class PackOverlay:
    directory: Annotated[str, 'Length = 1 (inclusive) and above']
    formats: InclusiveRange[int] | int | None = None
    min_format: PackFormat | None = None
    max_format: PackFormat | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::pack::PackOverlay": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "directory",
                "type": {
                    "kind": "string",
                    "lengthRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            },
            {
                "kind": "pair",
                "key": "formats",
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

