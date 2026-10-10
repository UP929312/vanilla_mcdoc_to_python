"""
Generated from symbols.json for ::java::data::worldgen::feature::DecoratedConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/DecoratedConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.FeatureRef import FeatureRef
    from vanilla_mcdoc.data.worldgen.feature.decorator.ConfiguredDecorator import ConfiguredDecorator


class DecoratedConfig(GeneratedModel):
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
