"""
Generated from symbols.json for ::java::assets::item_definition::TrimMaterial
Local link to file: vanilla_mcdoc/assets/item_definition/TrimMaterial.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.assets.item_definition.SelectCases import SelectCases
from vanilla_mcdoc.minecraft_types import IdSpec


class TrimMaterial(SelectCases[Annotated[str, IdSpec(registry='trim_material')]]):
    pass
