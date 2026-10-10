"""
Generated from symbols.json for ::java::util::text::ItemHoverContent
Local link to file: vanilla_mcdoc/util/text/ItemHoverContent.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownItemId import KnownItemId
    from vanilla_mcdoc.world.component.DataComponentPatch import DataComponentPatch


class ItemHoverContent(GeneratedModel):
    id: Annotated[str, IdSpec(registry='item')] | KnownItemId
    count: int | None = None
    components: DataComponentPatch | None = None
