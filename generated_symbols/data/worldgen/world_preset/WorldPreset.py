# Generated from symbols.json for ::java::data::worldgen::world_preset::WorldPreset
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.dimension.Dimension import Dimension


@dataclass(kw_only=True)
class WorldPreset:
    dimensions: dict[str, Dimension]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::world_preset::WorldPreset": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "dimensions",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": {
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
                                                        "value": "dimension"
                                                    }
                                                },
                                                "definition": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "boolean",
                                                        "value": True
                                                    }
                                                }
                                            }
                                        }
                                    }
                                ]
                            },
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::dimension::Dimension"
                            }
                        }
                    ]
                }
            }
        ]
    }
}

