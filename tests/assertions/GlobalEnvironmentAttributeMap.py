# ~~~ WHAT ARE WE TESTING ~~~

# A concrete type, with the values being type spec'd with the environment_attribute registry.
# Imports the IdSpec class properly too.

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::data::worldgen::attribute::GlobalEnvironmentAttributeMap
Local link to file: vanilla_mcdoc/data/worldgen/attribute/GlobalEnvironmentAttributeMap.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.data.worldgen.attribute.EnvironmentAttributeMap import EnvironmentAttributeMap
from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.registry.KnownEnvironmentAttributeId import KnownEnvironmentAttributeId


GlobalEnvironmentAttributeMap = EnvironmentAttributeMap[Annotated[str, IdSpec(registry='environment_attribute')] | KnownEnvironmentAttributeId]
