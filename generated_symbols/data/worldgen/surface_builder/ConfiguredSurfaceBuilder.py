"""
Generated from symbols.json for ::java::data::worldgen::surface_builder::ConfiguredSurfaceBuilder
Local link to file: generated_symbols/data/worldgen/surface_builder/ConfiguredSurfaceBuilder.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.util.block_state.BlockState import BlockState


@dataclass(kw_only=True)
class ConfigStruct:
    top_material: BlockState
    under_material: BlockState
    underwater_material: BlockState


@dataclass(kw_only=True)
class ConfiguredSurfaceBuilder:
    type: Annotated[str, IdSpec(registry='worldgen/surface_builder')]
    config: ConfigStruct


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

