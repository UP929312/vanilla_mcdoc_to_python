"""
Generated from symbols.json for ::java::data::block_transformer::BlockTransformParticle
Local link to file: generated_symbols/data/block_transformer/BlockTransformParticle.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class BlockTransformParticle(StrEnum):
    NONE = "none"
    SCRAPE = "scrape"
    WAXON = "wax_on"
    WAXOFF = "wax_off"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::block_transformer::BlockTransformParticle": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "None",
                "value": "none"
            },
            {
                "identifier": "Scrape",
                "value": "scrape"
            },
            {
                "identifier": "WaxOn",
                "value": "wax_on"
            },
            {
                "identifier": "WaxOff",
                "value": "wax_off"
            }
        ]
    }
}

