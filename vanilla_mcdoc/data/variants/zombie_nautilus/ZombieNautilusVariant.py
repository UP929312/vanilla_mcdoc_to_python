"""
Generated from symbols.json for ::java::data::variants::zombie_nautilus::ZombieNautilusVariant
Local link to file: vanilla_mcdoc/data/variants/zombie_nautilus/ZombieNautilusVariant.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from vanilla_mcdoc.data.variants.SpawnPrioritySelectors import SpawnPrioritySelectors
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.variants.zombie_nautilus.ZombieNautilusModelType import ZombieNautilusModelType


class ZombieNautilusVariant(SpawnPrioritySelectors):
    __resource_dir__: ClassVar[str] = 'zombie_nautilus_variant'

    model: ZombieNautilusModelType | None = None
    asset_id: Annotated[str, IdSpec(registry='texture')]  # The zombie nautilus texture to use for this variant.
