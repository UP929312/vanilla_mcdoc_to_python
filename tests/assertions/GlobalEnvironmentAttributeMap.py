# ~~~ WHAT ARE WE TESTING ~~~

# A concrete type, with the values being type spec'd with the environment_attribute registry.
# Imports the IdSpec class properly too.

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::data::worldgen::attribute::GlobalEnvironmentAttributeMap
Local link to file: generated_symbols/data/worldgen/attribute/GlobalEnvironmentAttributeMap.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from generated_symbols.data.worldgen.attribute.EnvironmentAttributeMap import EnvironmentAttributeMap
from generated_symbols.registry.KnownEnvironmentAttributeId import KnownEnvironmentAttributeId
from minecraft_registry import IdSpec


GlobalEnvironmentAttributeMap = EnvironmentAttributeMap[Annotated[str, IdSpec(registry='environment_attribute')] | KnownEnvironmentAttributeId]
