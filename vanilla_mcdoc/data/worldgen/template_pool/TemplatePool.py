"""
Generated from symbols.json for ::java::data::worldgen::template_pool::TemplatePool
Local link to file: vanilla_mcdoc/data/worldgen/template_pool/TemplatePool.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.template_pool.WeightedElement import WeightedElement


class TemplatePool(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/template_pool'

    name: str | None = None
    fallback: Annotated[str, IdSpec(registry='worldgen/template_pool')]
    elements: list[WeightedElement]
