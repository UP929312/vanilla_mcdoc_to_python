"""
Generated from symbols.json for ::java::world::component::item::RemoveEffectsConsumeEffect
Local link to file: vanilla_mcdoc/world/component/item/RemoveEffectsConsumeEffect.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class RemoveEffectsConsumeEffect(GeneratedModel):
    effects: Annotated[str, IdSpec(registry='mob_effect', tags='allowed')] | list[Annotated[str, IdSpec(registry='mob_effect')]]
