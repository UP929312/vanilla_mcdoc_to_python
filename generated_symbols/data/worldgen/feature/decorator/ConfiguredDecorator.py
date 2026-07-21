# Generated from symbols.json for ::java::data::worldgen::feature::decorator::ConfiguredDecorator
from dataclasses import dataclass
from typing import Any


@dataclass(kw_only=True)
class ConfiguredDecorator:
    type: str
    config: Any


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::decorator::ConfiguredDecorator": {
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
                                    "value": "worldgen/decorator"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "config",
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
                    "registry": "minecraft:decorator_config"
                }
            }
        ]
    }
}

