"""
Generated from symbols.json for ::java::data::advancement::RootAdvancementDisplay
Local link to file: vanilla_mcdoc/data/advancement/RootAdvancementDisplay.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.data.advancement.AdvancementDisplay import AdvancementDisplay
from vanilla_mcdoc.minecraft_types import IdSpec


class RootAdvancementDisplay(AdvancementDisplay):
    background: Annotated[str, IdSpec(registry='texture')]  # Used for the advancement tab.
