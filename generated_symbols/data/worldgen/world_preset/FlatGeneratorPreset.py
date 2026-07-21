# Generated from symbols.json for ::java::data::worldgen::world_preset::FlatGeneratorPreset
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.dimension.chunk_generator.FlatGeneratorSettings import FlatGeneratorSettings


@dataclass(kw_only=True)
class FlatGeneratorPreset:
    display: str
    settings: FlatGeneratorSettings


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::world_preset::FlatGeneratorPreset": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "display",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.2"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "item"
                                        }
                                    }
                                }
                            ]
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
                                            "value": "1.21.2"
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
                                                    "value": "item"
                                                }
                                            },
                                            "exclude": {
                                                "kind": "tree",
                                                "values": {
                                                    "0": {
                                                        "kind": "literal",
                                                        "value": {
                                                            "kind": "string",
                                                            "value": "air"
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "settings",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::dimension::chunk_generator::FlatGeneratorSettings"
                }
            }
        ]
    }
}

