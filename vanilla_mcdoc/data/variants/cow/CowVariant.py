"""
Generated from symbols.json for ::java::data::variants::cow::CowVariant
Local link to file: vanilla_mcdoc/data/variants/cow/CowVariant.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from vanilla_mcdoc.data.variants.SpawnPrioritySelectors import SpawnPrioritySelectors
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.variants.cow.CowModelType import CowModelType


class CowVariant(SpawnPrioritySelectors):
    __resource_dir__: ClassVar[str] = 'cow_variant'

    model: CowModelType | None = None
    asset_id: Annotated[str, IdSpec(registry='texture')]  # The cow texture to use for this variant.
    baby_asset_id: Annotated[str, IdSpec(registry='texture')]  # The baby cow texture to use for this variant.
