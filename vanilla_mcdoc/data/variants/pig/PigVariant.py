"""
Generated from symbols.json for ::java::data::variants::pig::PigVariant
Local link to file: vanilla_mcdoc/data/variants/pig/PigVariant.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from vanilla_mcdoc.data.variants.SpawnPrioritySelectors import SpawnPrioritySelectors
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.variants.pig.PigModelType import PigModelType


class PigVariant(SpawnPrioritySelectors):
    __resource_dir__: ClassVar[str] = 'pig_variant'

    model: PigModelType | None = None
    asset_id: Annotated[str, IdSpec(registry='texture')]  # The pig texture to use for this variant.
    baby_asset_id: Annotated[str, IdSpec(registry='texture')]  # The baby pig texture to use for this variant.
