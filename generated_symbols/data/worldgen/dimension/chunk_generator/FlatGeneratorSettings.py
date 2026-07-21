# Generated from symbols.json for ::java::data::worldgen::dimension::chunk_generator::FlatGeneratorSettings
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.dimension.chunk_generator.FlatGeneratorLayer import FlatGeneratorLayer


@dataclass(kw_only=True)
class FlatGeneratorSettings:
    layers: list[FlatGeneratorLayer]
    biome: str | None = None
    lakes: bool | None = None
    features: bool | None = None
    structure_overrides: list[str] | str | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::dimension::chunk_generator::FlatGeneratorSettings": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "biome",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "worldgen/biome"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "lakes",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "features",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "layers",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::dimension::chunk_generator::FlatGeneratorLayer"
                    }
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.18.2"
                            }
                        }
                    }
                ],
                "key": "structures",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::noise_settings::StructureSettings"
                }
            },
            {
                "kind": "pair",
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
                    }
                ],
                "key": "structure_overrides",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "list",
                            "item": {
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
                                                        "value": "worldgen/structure_set"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                ]
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
                                                    "value": "worldgen/structure_set"
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
                },
                "optional": True
            }
        ]
    }
}

