# Generated from symbols.json for ::java::data::worldgen::dimension::chunk_generator::FlatGeneratorLayer
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class FlatGeneratorLayer:
    height: Annotated[int, 'Range | `0`-`4096` | both inclusive']
    block: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::dimension::chunk_generator::FlatGeneratorLayer": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "height",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 4096
                    }
                }
            },
            {
                "kind": "pair",
                "key": "block",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "block"
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}

