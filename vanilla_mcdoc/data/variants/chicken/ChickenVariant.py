"""
Generated from symbols.json for ::java::data::variants::chicken::ChickenVariant
Local link to file: vanilla_mcdoc/data/variants/chicken/ChickenVariant.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from vanilla_mcdoc.data.variants.SpawnPrioritySelectors import SpawnPrioritySelectors
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.variants.chicken.ChickenModelType import ChickenModelType


class ChickenVariant(SpawnPrioritySelectors):
    __resource_dir__: ClassVar[str] = 'chicken_variant'

    model: ChickenModelType | None = None
    asset_id: Annotated[str, IdSpec(registry='texture')]  # The chicken texture to use for this variant.
    baby_asset_id: Annotated[str, IdSpec(registry='texture')]  # The baby chicken texture to use for this variant.
