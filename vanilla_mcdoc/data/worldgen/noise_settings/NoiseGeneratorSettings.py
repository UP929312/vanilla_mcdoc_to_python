"""
Generated from symbols.json for ::java::data::worldgen::noise_settings::NoiseGeneratorSettings
Local link to file: vanilla_mcdoc/data/worldgen/noise_settings/NoiseGeneratorSettings.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.material_rule.MaterialRuleRef import MaterialRuleRef
    from vanilla_mcdoc.data.worldgen.noise_settings.Aquifer import Aquifer
    from vanilla_mcdoc.data.worldgen.noise_settings.DebugFunctionEntry import DebugFunctionEntry
    from vanilla_mcdoc.data.worldgen.noise_settings.NoiseRouter import NoiseRouter
    from vanilla_mcdoc.data.worldgen.noise_settings.NoiseSettings import NoiseSettings
    from vanilla_mcdoc.data.worldgen.noise_settings.SpawnTargetPoint import SpawnTargetPoint
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class NoiseGeneratorSettings(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/noise_settings'

    default_fluid: BlockState
    sea_level: int
    disable_mob_generation: bool  # If true, mobs will not spawn during generation.
    aquifers: Aquifer | None = None
    legacy_random_source: bool
    noise: NoiseSettings
    noise_router: NoiseRouter
    spawn_target: list[SpawnTargetPoint]
    material_rule: MaterialRuleRef
    debug_functions: list[DebugFunctionEntry] | None = None
