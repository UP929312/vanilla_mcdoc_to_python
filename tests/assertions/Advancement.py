# ~~~ WHAT ARE WE TESTING ~~~

# Tests the criteria field, which is a mapping of 

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::data::advancement::Advancement
Local link to file: generated_symbols/data/advancement/Advancement.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.advancement.AdvancementCriterion import AdvancementCriterion
    from generated_symbols.data.advancement.AdvancementDisplay import AdvancementDisplay
    from generated_symbols.data.advancement.AdvancementRewards import AdvancementRewards
    from generated_symbols.data.advancement.RootAdvancementDisplay import RootAdvancementDisplay


class Advancement(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'advancement'

    parent: Annotated[str, IdSpec(registry='advancement')] | None = None  # If this field is absent, this advancement is a root advancement. Circular references cause a loading failure.
    display: RootAdvancementDisplay | AdvancementDisplay | None = None  # If present, advancement will be visible in the advancement tabs.
    criteria: dict[str, AdvancementCriterion]  # If `requirements` is not defined, all defined criteria will be required.
    requirements: Annotated[list[Annotated[list[str], Field(min_length=1)]], Field(min_length=1)] | None = None  # If all criteria are required at once, this may be omitted.  Contains all of the `criteria` keys.  If all of the lists each have at least one criteria met, the advancement is complete (basically AND grouping of OR groups).
    rewards: AdvancementRewards | None = None  # Provided to the player when this advancement is obtained.
    sends_telemetry_event: bool | None = None  # Defaults to `false`. The vanilla game client only reads this for advancements from the `minecraft` namespace.
