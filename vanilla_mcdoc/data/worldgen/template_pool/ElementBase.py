"""
Generated from symbols.json for ::java::data::worldgen::template_pool::ElementBase
Local link to file: vanilla_mcdoc/data/worldgen/template_pool/ElementBase.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.template_pool.Projection import Projection


class ElementBase(GeneratedModel):
    projection: Projection


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::template_pool::ElementBase": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "projection",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::template_pool::Projection"
                }
            }
        ]
    }
}
