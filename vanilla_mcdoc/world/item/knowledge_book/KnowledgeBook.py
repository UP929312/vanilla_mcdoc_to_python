"""
Generated from symbols.json for ::java::world::item::knowledge_book::KnowledgeBook
Local link to file: vanilla_mcdoc/world/item/knowledge_book/KnowledgeBook.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.world.item.ItemBase import ItemBase


class KnowledgeBook(ItemBase):
    Recipes: list[Annotated[str, IdSpec(registry='recipe')]] | None = None
