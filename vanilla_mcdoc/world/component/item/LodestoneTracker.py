"""
Generated from symbols.json for ::java::world::component::item::LodestoneTracker
Local link to file: vanilla_mcdoc/world/component/item/LodestoneTracker.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.GlobalPos import GlobalPos


class LodestoneTracker(GeneratedModel):
    target: GlobalPos | None = None  # Location of the lodestone. Optional. If not set, the compass will spin randomly.
    tracked: bool | None = None  # When `true`, the component is removed when the lodestone is broken. When `false`, the component is kept. Defaults to true.
