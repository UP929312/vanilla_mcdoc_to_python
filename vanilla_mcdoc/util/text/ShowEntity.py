"""
Generated from symbols.json for ::java::util::text::ShowEntity
Local link to file: vanilla_mcdoc/util/text/ShowEntity.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec, MinecraftUUID, MinecraftUUIDString

if TYPE_CHECKING:
    from vanilla_mcdoc.util.text.Text import Text


class ShowEntity(GeneratedModel):
    id: Annotated[str, IdSpec(registry='entity_type')]
    uuid: MinecraftUUID | MinecraftUUIDString
    name: Text | None = None
