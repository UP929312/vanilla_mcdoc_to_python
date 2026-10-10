"""
Generated from symbols.json for ::java::data::worldgen::noise_settings::SpawnTargetPoint
Local link to file: vanilla_mcdoc/data/worldgen/noise_settings/SpawnTargetPoint.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.dimension.biome_source.ClimateParameter import ClimateParameter


type SpawnTargetPoint = dict[Annotated[str, IdSpec(registry='worldgen/density_function')], ClimateParameter]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::noise_settings::SpawnTargetPoint": {
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
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "worldgen/density_function"
                                }
                            }
                        }
                    ]
                },
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::dimension::biome_source::ClimateParameter"
                }
            }
        ]
    }
}
