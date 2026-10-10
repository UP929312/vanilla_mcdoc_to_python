"""
Generated from symbols.json for ::java::data::trim::TrimPattern
Local link to file: vanilla_mcdoc/data/trim/TrimPattern.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.util.text.Text import Text


class TrimPattern(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'trim_pattern'

    asset_id: Annotated[str, IdSpec()]  # ID of the pattern that will be used in the resource pack as an overlay on the armor.  The texture is located under `trims/entity/<layer>/`.
    description: Text  # Text displayed in the item tooltip.
    decal: bool | None = None  # Whether the pattern texture will be masked based on the underlying armor. Defaults to `false`.
