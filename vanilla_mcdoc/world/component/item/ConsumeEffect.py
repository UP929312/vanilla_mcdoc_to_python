"""
Generated from symbols.json for ::java::world::component::item::ConsumeEffect
Local link to file: vanilla_mcdoc/world/component/item/ConsumeEffect.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import GeneratedModel, tag_of
from vanilla_mcdoc.world.component.item.ApplyEffectsConsumeEffect import ApplyEffectsConsumeEffect
from vanilla_mcdoc.world.component.item.PlaySoundConsumeEffect import PlaySoundConsumeEffect
from vanilla_mcdoc.world.component.item.RemoveEffectsConsumeEffect import RemoveEffectsConsumeEffect
from vanilla_mcdoc.world.component.item.TeleportRandomlyConsumeEffect import TeleportRandomlyConsumeEffect


class ConsumeEffectApplyEffects(ApplyEffectsConsumeEffect):
    type: Literal['minecraft:apply_effects', 'apply_effects'] = 'minecraft:apply_effects'


class ConsumeEffectClearAllEffects(GeneratedModel):
    type: Literal['minecraft:clear_all_effects', 'clear_all_effects'] = 'minecraft:clear_all_effects'


class ConsumeEffectPlaySound(PlaySoundConsumeEffect):
    type: Literal['minecraft:play_sound', 'play_sound'] = 'minecraft:play_sound'


class ConsumeEffectRemoveEffects(RemoveEffectsConsumeEffect):
    type: Literal['minecraft:remove_effects', 'remove_effects'] = 'minecraft:remove_effects'


class ConsumeEffectTeleportRandomly(TeleportRandomlyConsumeEffect):
    type: Literal['minecraft:teleport_randomly', 'teleport_randomly'] = 'minecraft:teleport_randomly'


type ConsumeEffect = Annotated[
    Annotated[ConsumeEffectApplyEffects, Tag('minecraft:apply_effects')]
    | Annotated[ConsumeEffectClearAllEffects, Tag('minecraft:clear_all_effects')]
    | Annotated[ConsumeEffectPlaySound, Tag('minecraft:play_sound')]
    | Annotated[ConsumeEffectRemoveEffects, Tag('minecraft:remove_effects')]
    | Annotated[ConsumeEffectTeleportRandomly, Tag('minecraft:teleport_randomly')],
    Discriminator(tag_of('type')),
]
