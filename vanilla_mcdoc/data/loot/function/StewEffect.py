"""
Generated from symbols.json for ::java::data::loot::function::StewEffect
Local link to file: vanilla_mcdoc/data/loot/function/StewEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.IntNumberProviderRef import IntNumberProviderRef


class StewEffect(GeneratedModel):
    type: Annotated[str, IdSpec(registry='mob_effect')]  # The status effect of this stew effect.
    duration: IntNumberProviderRef  # The duration of this stew effect, in seconds.
