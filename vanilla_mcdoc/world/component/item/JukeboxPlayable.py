"""
Generated from symbols.json for ::java::world::component::item::JukeboxPlayable
Local link to file: vanilla_mcdoc/world/component/item/JukeboxPlayable.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class JukeboxPlayable(GeneratedModel):
    song: Annotated[str, IdSpec(registry='jukebox_song')]
    show_in_tooltip: bool | None = None
