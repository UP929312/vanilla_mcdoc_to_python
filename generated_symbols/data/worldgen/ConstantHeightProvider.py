# Generated from symbols.json for ::java::data::worldgen::ConstantHeightProvider
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.VerticalAnchor import VerticalAnchor


@dataclass(kw_only=True)
class ConstantHeightProvider:
    value: VerticalAnchor


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::ConstantHeightProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "value",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::VerticalAnchor"
                }
            }
        ]
    }
}

