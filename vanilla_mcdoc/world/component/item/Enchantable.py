"""
Generated from symbols.json for ::java::world::component::item::Enchantable
Local link to file: vanilla_mcdoc/world/component/item/Enchantable.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class Enchantable(GeneratedModel):
    value: Annotated[int, Field(ge=1)]
