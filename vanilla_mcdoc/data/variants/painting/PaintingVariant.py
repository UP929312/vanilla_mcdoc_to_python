"""
Generated from symbols.json for ::java::data::variants::painting::PaintingVariant
Local link to file: vanilla_mcdoc/data/variants/painting/PaintingVariant.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.util.text.Text import Text


class PaintingVariant(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'painting_variant'

    asset_id: Annotated[str, IdSpec(registry='texture', path='painting/')]
    width: Annotated[int, Field(ge=1, le=16)]  # Dimension in blocks.
    height: Annotated[int, Field(ge=1, le=16)]  # Dimension in blocks.
    title: Text | None = None
    author: Text | None = None
