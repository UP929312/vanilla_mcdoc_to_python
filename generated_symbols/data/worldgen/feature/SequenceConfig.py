# Generated from symbols.json for ::java::data::worldgen::feature::SequenceConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.placement.PlacedFeatureRef import PlacedFeatureRef


@dataclass(kw_only=True)
class SequenceConfig:
    features: Annotated[list[PlacedFeatureRef], 'Length = 1 (inclusive) and above'] | str  # The features to generate, in order.  If any feature in the list is not placed, the following features will also be skipped.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::SequenceConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The features to generate, in order. \\\nIf any feature in the list is not placed, the following features will also be skipped.",
                "key": "features",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "list",
                            "item": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::feature::placement::PlacedFeatureRef"
                            },
                            "lengthRange": {
                                "kind": 0,
                                "min": 1
                            }
                        },
                        {
                            "kind": "string",
                            "attributes": [
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

