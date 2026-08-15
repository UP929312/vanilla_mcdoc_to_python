"""
Generated from symbols.json for ::java::data::worldgen::surface_builder::ConfiguredSurfaceBuilderRef
Local link to file: generated_symbols/data/worldgen/surface_builder/ConfiguredSurfaceBuilderRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.surface_builder.ConfiguredSurfaceBuilder import ConfiguredSurfaceBuilder


type ConfiguredSurfaceBuilderRef = Annotated[str, IdSpec(registry='worldgen/configured_surface_builder')] | ConfiguredSurfaceBuilder


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::surface_builder::ConfiguredSurfaceBuilderRef": {
        "kind": "union",
        "members": [
            {
                "kind": "string",
                "attributes": [
                    {
                        "name": "id",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "worldgen/configured_surface_builder"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "reference",
                "path": "::java::data::worldgen::surface_builder::ConfiguredSurfaceBuilder"
            }
        ]
    }
}

