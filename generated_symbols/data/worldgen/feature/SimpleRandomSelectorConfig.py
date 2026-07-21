# Generated from symbols.json for ::java::data::worldgen::feature::SimpleRandomSelectorConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.FeatureRef import FeatureRef


@dataclass(kw_only=True)
class SimpleRandomSelectorConfig:
    features: list[FeatureRef] | str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::SimpleRandomSelectorConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "features",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "list",
                            "item": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::feature::FeatureRef"
                            }
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.18.2"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "registry": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "worldgen/placed_feature"
                                                }
                                            },
                                            "tags": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "allowed"
                                                }
                                            }
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

