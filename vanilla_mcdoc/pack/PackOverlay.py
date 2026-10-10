"""
Generated from symbols.json for ::java::pack::PackOverlay
Local link to file: vanilla_mcdoc/pack/PackOverlay.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.pack.PackFormat import PackFormat
    from vanilla_mcdoc.util.InclusiveRange import InclusiveRange


class PackOverlay(GeneratedModel):
    directory: Annotated[str, Field(min_length=1)]
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
