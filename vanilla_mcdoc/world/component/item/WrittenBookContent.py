"""
Generated from symbols.json for ::java::world::component::item::WrittenBookContent
Local link to file: vanilla_mcdoc/world/component/item/WrittenBookContent.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.Filterable import Filterable
    from vanilla_mcdoc.util.text.Text import Text
    from vanilla_mcdoc.world.component.item.BookGeneration import BookGeneration


class WrittenBookContent(GeneratedModel):
    pages: list[Filterable[Text]] | None = None
    title: Filterable[Annotated[str, Field(max_length=32)]]
    author: str
    generation: BookGeneration | None = None  # Number of times this written book has been copied. Defaults to 0. If the value is greater than 1, the book cannot be copied.
    resolved: bool | None = None  # Whether the dynamic content on the pages has been resolved.
