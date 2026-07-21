# Generated from symbols.json for ::java::data::worldgen::surface_builder::ConfiguredSurfaceBuilder
from dataclasses import dataclass
from typing import Any


@dataclass(kw_only=True)
class ConfiguredSurfaceBuilder:
    type: str
    config: Any


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::surface_builder::ConfiguredSurfaceBuilder": {
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
                                    "value": "worldgen/surface_builder"
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
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "top_material",
                            "type": {
                                "kind": "reference",
                                "path": "::java::util::block_state::BlockState"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "under_material",
                            "type": {
                                "kind": "reference",
                                "path": "::java::util::block_state::BlockState"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "underwater_material",
                            "type": {
                                "kind": "reference",
                                "path": "::java::util::block_state::BlockState"
                            }
                        }
                    ]
                }
            }
        ]
    }
}

