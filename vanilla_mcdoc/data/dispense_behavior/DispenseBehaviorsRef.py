"""
Generated from symbols.json for ::java::data::dispense_behavior::DispenseBehaviorsRef
Local link to file: vanilla_mcdoc/data/dispense_behavior/DispenseBehaviorsRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.dispense_behavior.DispenseBehavior import DispenseBehavior
    from vanilla_mcdoc.registry.KnownDispenseBehaviorId import KnownDispenseBehaviorId


type DispenseBehaviorsRef = Annotated[str, IdSpec(registry='dispense_behavior')] | KnownDispenseBehaviorId | list[DispenseBehavior]
