"""
Generated from symbols.json for ::java::assets::item_definition::ContextEntityType
Local link to file: vanilla_mcdoc/assets/item_definition/ContextEntityType.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.assets.item_definition.SelectCases import SelectCases
from vanilla_mcdoc.minecraft_types import IdSpec


class ContextEntityType(SelectCases[Annotated[str, IdSpec(registry='entity_type')]]):
    pass
