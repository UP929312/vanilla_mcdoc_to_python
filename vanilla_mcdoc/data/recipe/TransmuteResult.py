"""
Generated from symbols.json for ::java::data::recipe::TransmuteResult
Local link to file: vanilla_mcdoc/data/recipe/TransmuteResult.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.DataComponentPatch import DataComponentPatch


class TransmuteResult(GeneratedModel):
    id: Annotated[str, IdSpec(registry='item', exclude=('air',))] | None = None  # Defaults to the input item.
    count: Annotated[int, Field(ge=1, le=99)] | None = None  # Defaults to `1`.
    components: DataComponentPatch | None = None
