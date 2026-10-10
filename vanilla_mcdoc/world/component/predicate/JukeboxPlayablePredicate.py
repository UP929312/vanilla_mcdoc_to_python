"""
Generated from symbols.json for ::java::world::component::predicate::JukeboxPlayablePredicate
Local link to file: vanilla_mcdoc/world/component/predicate/JukeboxPlayablePredicate.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class JukeboxPlayablePredicate(GeneratedModel):
    song: Annotated[str, IdSpec(registry='jukebox_song', tags='allowed')] | list[Annotated[str, IdSpec(registry='jukebox_song')]] | None = None
