# Generated from symbols.json for ::java::data::worldgen::surface_builder::ConfiguredSurfaceBuilderRef
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.surface_builder.ConfiguredSurfaceBuilder import ConfiguredSurfaceBuilder


type ConfiguredSurfaceBuilderRef = str | ConfiguredSurfaceBuilder


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

