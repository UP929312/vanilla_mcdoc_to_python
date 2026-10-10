"""
Generated from symbols.json for ::java::data::worldgen::feature::CoralConfig
Local link to file: generated_symbols/data/worldgen/feature/CoralConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.placement.PlacedFeatureRef import PlacedFeatureRef


class CoralConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    feature: PlacedFeatureRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::CoralConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "feature",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::placement::PlacedFeatureRef"
                }
            }
        ]
    }
}
