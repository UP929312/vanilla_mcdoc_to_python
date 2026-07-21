# Generated from symbols.json for ::java::data::worldgen::HeightProvider
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.VerticalAnchor import VerticalAnchor


@dataclass(kw_only=True)
class HeightProviderStruct1:
    type: str

type HeightProvider = HeightProviderStruct1 | VerticalAnchor


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::HeightProvider": {
        "kind": "union",
        "members": [
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "type",
                        "type": {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "height_provider_type"
                                        }
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "kind": "spread",
                        "type": {
                            "kind": "dispatcher",
                            "parallelIndices": [
                                {
                                    "kind": "dynamic",
                                    "accessor": [
                                        "type"
                                    ]
                                }
                            ],
                            "registry": "minecraft:height_provider"
                        }
                    }
                ]
            },
            {
                "kind": "reference",
                "path": "::java::data::worldgen::VerticalAnchor"
            }
        ]
    }
}

