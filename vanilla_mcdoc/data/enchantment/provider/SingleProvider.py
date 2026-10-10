"""
Generated from symbols.json for ::java::data::enchantment::provider::SingleProvider
Local link to file: vanilla_mcdoc/data/enchantment/provider/SingleProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider


class SingleProvider(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'enchantment_provider'

    enchantment: Annotated[str, IdSpec(registry='enchantment')]
    level: IntProvider[int] | int
