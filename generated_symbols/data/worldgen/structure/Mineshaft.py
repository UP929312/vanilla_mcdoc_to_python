"""
Generated from symbols.json for ::java::data::worldgen::structure::Mineshaft
Local link to file: generated_symbols/data/worldgen/structure/Mineshaft.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.structure.MineshaftType import MineshaftType


class Mineshaft(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    mineshaft_type: MineshaftType


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure::Mineshaft": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "type",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::structure::MineshaftType"
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
                "key": "mineshaft_type",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::structure::MineshaftType"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "probability",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            }
        ]
    }
}

