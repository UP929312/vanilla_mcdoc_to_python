"""
Generated from symbols.json for ::java::data::worldgen::world_preset::WorldPreset
Local link to file: generated_symbols/data/worldgen/world_preset/WorldPreset.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.dimension.Dimension import Dimension


class WorldPreset(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/world_preset'

    dimensions: dict[Annotated[str, IdSpec(registry='dimension', definition=True)], Dimension]


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

