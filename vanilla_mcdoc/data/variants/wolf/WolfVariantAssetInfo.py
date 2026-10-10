"""
Generated from symbols.json for ::java::data::variants::wolf::WolfVariantAssetInfo
Local link to file: vanilla_mcdoc/data/variants/wolf/WolfVariantAssetInfo.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class WolfVariantAssetInfo(GeneratedModel):
    wild: Annotated[str, IdSpec(registry='texture')]
    tame: Annotated[str, IdSpec(registry='texture')]
    angry: Annotated[str, IdSpec(registry='texture')]
