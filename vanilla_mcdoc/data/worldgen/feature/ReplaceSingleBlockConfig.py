"""
Generated from symbols.json for ::java::data::worldgen::feature::ReplaceSingleBlockConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/ReplaceSingleBlockConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.TargetBlock import TargetBlock


class ReplaceSingleBlockConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    targets: list[TargetBlock]
