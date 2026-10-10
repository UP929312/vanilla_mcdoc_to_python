# ~~~ WHAT ARE WE TESTING ~~~

# Points to the registry nicely

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::world::entity::mob::AttributeModifier
Local link to file: vanilla_mcdoc/world/entity/mob/AttributeModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.util.attribute.AttributeOperation import AttributeOperation


class AttributeModifier(GeneratedModel):
    id: Annotated[str, IdSpec(registry='attribute_modifier')]  # The unique identifier of this attribute modifier.
    amount: float  # Change in the attribute.
    operation: AttributeOperation  # The operation used for this modifier.
