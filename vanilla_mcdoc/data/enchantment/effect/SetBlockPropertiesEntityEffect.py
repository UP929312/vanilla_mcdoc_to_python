"""
Generated from symbols.json for ::java::data::enchantment::effect::SetBlockPropertiesEntityEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect/SetBlockPropertiesEntityEffect.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class SetBlockPropertiesEntityEffect(GeneratedModel):
    properties: dict[str, str]
    offset: tuple[int, int, int] | None = None  # Relative coordinates to offset the block by. Defaults to `[0, 0, 0]`.
    trigger_game_event: Annotated[str, IdSpec(registry='game_event')] | None = None  # Defaults to no game event dispatched.
