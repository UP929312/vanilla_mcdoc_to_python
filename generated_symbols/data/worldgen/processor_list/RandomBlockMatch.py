"""
Generated from symbols.json for ::java::data::worldgen::processor_list::RandomBlockMatch
Local link to file: generated_symbols/data/worldgen/processor_list/RandomBlockMatch.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.registry.KnownBlockId import KnownBlockId


class RandomBlockMatch(GeneratedModel):
    block: Annotated[str, IdSpec(registry='block')] | KnownBlockId
    probability: Annotated[float, Field(ge=0, le=1)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::RandomBlockMatch": {
        "kind": "struct",
        "fields": [
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
            },
            {
                "kind": "pair",
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

