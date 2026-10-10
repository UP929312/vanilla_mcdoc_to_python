"""
Generated from symbols.json for ::java::data::variants::wolf::WolfVariant
Local link to file: vanilla_mcdoc/data/variants/wolf/WolfVariant.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.data.variants.SpawnPrioritySelectors import SpawnPrioritySelectors

if TYPE_CHECKING:
    from vanilla_mcdoc.data.variants.wolf.WolfVariantAssetInfo import WolfVariantAssetInfo


class WolfVariant(SpawnPrioritySelectors):
    __resource_dir__: ClassVar[str] = 'wolf_variant'

    assets: WolfVariantAssetInfo  # The texture set to use for this wolf variant.
    baby_assets: WolfVariantAssetInfo  # The baby texture set to use for this wolf variant.
