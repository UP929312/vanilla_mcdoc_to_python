"""
Generated from symbols.json for ::java::util::text::EntityHoverContent
Local link to file: vanilla_mcdoc/util/text/EntityHoverContent.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec, MinecraftUUID, MinecraftUUIDString

if TYPE_CHECKING:
    from vanilla_mcdoc.util.text.Text import Text


class EntityHoverContent(GeneratedModel):
    type: Annotated[str, IdSpec(registry='entity_type')]
    id: MinecraftUUID | MinecraftUUIDString
    name: Text | None = None
