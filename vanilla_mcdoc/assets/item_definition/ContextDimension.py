"""
Generated from symbols.json for ::java::assets::item_definition::ContextDimension
Local link to file: vanilla_mcdoc/assets/item_definition/ContextDimension.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.assets.item_definition.SelectCases import SelectCases
from vanilla_mcdoc.minecraft_types import IdSpec


class ContextDimension(SelectCases[Annotated[str, IdSpec(registry='dimension')]]):
    pass
