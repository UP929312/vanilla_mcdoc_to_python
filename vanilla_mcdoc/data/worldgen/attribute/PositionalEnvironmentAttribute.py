"""
Generated from symbols.json for ::java::data::worldgen::attribute::PositionalEnvironmentAttribute
Local link to file: vanilla_mcdoc/data/worldgen/attribute/PositionalEnvironmentAttribute.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.minecraft_types import IdSpec


type PositionalEnvironmentAttribute = Annotated[str, IdSpec(registry='environment_attribute', exclude=('gameplay/fast_lava', 'gameplay/sky_light_level'))]
