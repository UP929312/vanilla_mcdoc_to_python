# Generated from symbols.json for ::java::data::worldgen::feature::decorator::DecoratedConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.decorator.ConfiguredDecorator import ConfiguredDecorator


@dataclass(kw_only=True)
class DecoratedConfig:
    outer: ConfiguredDecorator
    inner: ConfiguredDecorator


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::decorator::DecoratedConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "outer",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::decorator::ConfiguredDecorator"
                }
            },
            {
                "kind": "pair",
                "key": "inner",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::decorator::ConfiguredDecorator"
                }
            }
        ]
    }
}

