# Generated from symbols.json for ::java::data::worldgen::feature::decorator::RangeConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.HeightProvider import HeightProvider


@dataclass(kw_only=True)
class RangeConfig:
    height: HeightProvider


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::decorator::RangeConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "height",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::HeightProvider"
                }
            }
        ],
        "attributes": [
            {
                "name": "since",
                "value": {
                    "kind": "literal",
                    "value": {
                        "kind": "string",
                        "value": "1.17"
                    }
                }
            }
        ]
    }
}

