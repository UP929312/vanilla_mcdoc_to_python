"""
Generated from symbols.json for ::java::data::worldgen::noise_settings::StructureSettings
Local link to file: vanilla_mcdoc/data/worldgen/noise_settings/StructureSettings.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.structure_set.ConcentricRingsPlacement import ConcentricRingsPlacement
    from vanilla_mcdoc.data.worldgen.structure_set.RandomSpreadPlacement import RandomSpreadPlacement


class StructureSettings(GeneratedModel):
    stronghold: ConcentricRingsPlacement | None = None
    structures: dict[Annotated[str, IdSpec(registry='worldgen/structure_feature')], RandomSpreadPlacement]
