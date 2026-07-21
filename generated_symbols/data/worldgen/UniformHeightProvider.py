# Generated from symbols.json for ::java::data::worldgen::UniformHeightProvider
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.VerticalAnchor import VerticalAnchor


@dataclass(kw_only=True)
class UniformHeightProvider:
    min_inclusive: VerticalAnchor
    max_inclusive: VerticalAnchor


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::UniformHeightProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "min_inclusive",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::VerticalAnchor"
                }
            },
            {
                "kind": "pair",
                "key": "max_inclusive",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::VerticalAnchor"
                }
            }
        ]
    }
}

