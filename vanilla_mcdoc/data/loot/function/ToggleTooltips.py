"""
Generated from symbols.json for ::java::data::loot::function::ToggleTooltips
Local link to file: vanilla_mcdoc/data/loot/function/ToggleTooltips.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.data.loot.function.Conditions import Conditions
from vanilla_mcdoc.minecraft_types import IdSpec


class ToggleTooltips(Conditions):
    toggles: dict[Annotated[str, IdSpec(registry='data_component_type')], bool]  # Toggles which tooltips are shown.
