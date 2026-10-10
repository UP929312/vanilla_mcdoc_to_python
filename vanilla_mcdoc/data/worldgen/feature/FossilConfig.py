"""
Generated from symbols.json for ::java::data::worldgen::feature::FossilConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/FossilConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.processor_list.ProcessorListRef import ProcessorListRef


class FossilConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    max_empty_corners_allowed: Annotated[int, Field(ge=0, le=7)]  # If more corners are exposed to air, feature placement is cancelled.
    fossil_structures: list[Annotated[str, IdSpec(registry='structure')]]
    overlay_structures: list[Annotated[str, IdSpec(registry='structure')]]
    fossil_processors: ProcessorListRef
    overlay_processors: ProcessorListRef
