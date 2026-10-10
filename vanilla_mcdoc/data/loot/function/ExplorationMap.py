"""
Generated from symbols.json for ::java::data::loot::function::ExplorationMap
Local link to file: vanilla_mcdoc/data/loot/function/ExplorationMap.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.data.loot.function.Conditions import Conditions
from vanilla_mcdoc.minecraft_types import IdSpec


class ExplorationMap(Conditions):
    destination: Annotated[str, IdSpec(registry='worldgen/structure', tags='allowed')] | list[Annotated[str, IdSpec(registry='worldgen/structure')]]  # Generated structure to locate. Accepts any of the structure types used by the `/locate` command.
    decoration: Annotated[str, IdSpec(registry='map_decoration_type')] | None = None  # The icon used to mark the destination on the map.
    zoom: int | None = None  # Defaults to 2.
    search_radius: int | None = None  # The size, in chunks, of the area to search for structures. The area checked is square, not circular. Radius `0` causes only the current chunk to be searched, radius `1` causes the current chunk and eight adjacent chunks to be searched, and so on. Defaults to `50`.
    skip_existing_chunks: bool | None = None  # Whether to not search in chunks that have already been generated. Defaults to `true`.
