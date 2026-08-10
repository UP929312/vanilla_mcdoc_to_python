# ~~~ WHAT ARE WE TESTING ~~~

# A concrete type, with the values being type spec'd with the environment_attribute registry.
# Imports the IdSpec class properly too.

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::data::worldgen::attribute::GlobalEnvironmentAttributeMap
Local link to file: generated_symbols/data/worldgen/attribute/GlobalEnvironmentAttributeMap.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.attribute.EnvironmentAttributeMap import EnvironmentAttributeMap


GlobalEnvironmentAttributeMap = EnvironmentAttributeMap[Annotated[str, IdSpec(registry='environment_attribute')]]
