"""
Generated from symbols.json for ::java::data::worldgen::dimension::chunk_generator::FlatGeneratorLayer
Local link to file: generated_symbols/data/worldgen/dimension/chunk_generator/FlatGeneratorLayer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.registry.KnownBlockId import KnownBlockId


class FlatGeneratorLayer(GeneratedModel):
    height: Annotated[int, Field(ge=0, le=4096)]
    block: Annotated[str, IdSpec(registry='block')] | KnownBlockId


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

