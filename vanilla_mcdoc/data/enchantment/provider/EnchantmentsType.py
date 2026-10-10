"""
Generated from symbols.json for ::java::data::enchantment::provider::EnchantmentsType
Local link to file: vanilla_mcdoc/data/enchantment/provider/EnchantmentsType.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.minecraft_types import IdSpec


type EnchantmentsType = Annotated[str, IdSpec(registry='enchantment', tags='allowed')] | Annotated[list[Annotated[str, IdSpec(registry='enchantment')]], Field(min_length=1)]
