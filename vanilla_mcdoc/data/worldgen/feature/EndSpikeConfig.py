"""
Generated from symbols.json for ::java::data::worldgen::feature::EndSpikeConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/EndSpikeConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.EndSpike import EndSpike


class EndSpikeConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    spikes: list[EndSpike]
    crystal_invulnerable: bool | None = None
    crystal_beam_target: tuple[int, int, int] | None = None
