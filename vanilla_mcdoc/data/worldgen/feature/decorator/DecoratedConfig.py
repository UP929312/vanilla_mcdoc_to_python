"""
Generated from symbols.json for ::java::data::worldgen::feature::decorator::DecoratedConfig
Local link to file: generated_symbols/data/worldgen/feature/decorator/DecoratedConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.decorator.ConfiguredDecorator import ConfiguredDecorator


class DecoratedConfig(GeneratedModel):
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
