"""
Generated from symbols.json for ::java::world::component::item::WritableBookContent
Local link to file: vanilla_mcdoc/world/component/item/WritableBookContent.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.Filterable import Filterable


class WritableBookContent(GeneratedModel):
    pages: list[Filterable[str]]
