# Generated from symbols.json for ::java::data::worldgen::template_pool::ElementBase
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.template_pool.Projection import Projection


@dataclass(kw_only=True)
class ElementBase:
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

