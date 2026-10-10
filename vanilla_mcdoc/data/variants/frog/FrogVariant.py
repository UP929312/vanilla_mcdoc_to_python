"""
Generated from symbols.json for ::java::data::variants::frog::FrogVariant
Local link to file: vanilla_mcdoc/data/variants/frog/FrogVariant.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar

from vanilla_mcdoc.data.variants.SpawnPrioritySelectors import SpawnPrioritySelectors
from vanilla_mcdoc.minecraft_types import IdSpec


class FrogVariant(SpawnPrioritySelectors):
    __resource_dir__: ClassVar[str] = 'frog_variant'

    asset_id: Annotated[str, IdSpec(registry='texture')]  # The frog texture to use for this variant.
