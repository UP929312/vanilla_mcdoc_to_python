# Generated from symbols.json for ::java::data::worldgen::feature::DecoratedConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.FeatureRef import FeatureRef
    from generated_symbols.data.worldgen.feature.decorator.ConfiguredDecorator import ConfiguredDecorator


@dataclass(kw_only=True)
class DecoratedConfig:
    decorator: ConfiguredDecorator
    feature: FeatureRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::DecoratedConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "decorator",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::decorator::ConfiguredDecorator"
                }
            },
            {
                "kind": "pair",
                "key": "feature",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::FeatureRef"
                }
            }
        ]
    }
}

