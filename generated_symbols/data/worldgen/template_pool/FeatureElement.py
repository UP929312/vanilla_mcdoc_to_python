# Generated from symbols.json for ::java::data::worldgen::template_pool::FeatureElement
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.worldgen.template_pool.ElementBase import ElementBase

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.placement.PlacedFeatureRef import PlacedFeatureRef


@dataclass(kw_only=True)
class FeatureElement(ElementBase):
    feature: PlacedFeatureRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::template_pool::FeatureElement": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::template_pool::ElementBase"
                }
            },
            {
                "kind": "pair",
                "key": "feature",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::data::worldgen::feature::ConfiguredFeatureRef",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.18"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::data::worldgen::feature::placement::PlacedFeatureRef",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.18"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }
}

