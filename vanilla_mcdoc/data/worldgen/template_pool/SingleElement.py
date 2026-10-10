"""
Generated from symbols.json for ::java::data::worldgen::template_pool::SingleElement
Local link to file: vanilla_mcdoc/data/worldgen/template_pool/SingleElement.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.data.worldgen.template_pool.ElementBase import ElementBase
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.processor_list.ProcessorListRef import ProcessorListRef
    from vanilla_mcdoc.data.worldgen.structure.LiquidSettings import LiquidSettings


class SingleElement(ElementBase):
    location: Annotated[str, IdSpec(registry='structure')]
    processors: ProcessorListRef
    override_liquid_settings: LiquidSettings | None = None
