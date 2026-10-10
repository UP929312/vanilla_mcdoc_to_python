"""
Generated from symbols.json for ::java::data::variants::cat::CatVariant
Local link to file: vanilla_mcdoc/data/variants/cat/CatVariant.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar

from vanilla_mcdoc.data.variants.SpawnPrioritySelectors import SpawnPrioritySelectors
from vanilla_mcdoc.minecraft_types import IdSpec


class CatVariant(SpawnPrioritySelectors):
    __resource_dir__: ClassVar[str] = 'cat_variant'

    asset_id: Annotated[str, IdSpec(registry='texture')]  # The cat texture to use for this variant.
    baby_asset_id: Annotated[str, IdSpec(registry='texture')]  # The baby cat texture to use for this variant.
