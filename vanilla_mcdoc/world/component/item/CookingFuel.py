"""
Generated from symbols.json for ::java::world::component::item::CookingFuel
Local link to file: vanilla_mcdoc/world/component/item/CookingFuel.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownContextFloatProviderId import KnownContextFloatProviderId
    from vanilla_mcdoc.registry.KnownContextIntProviderId import KnownContextIntProviderId


class CookingFuel(GeneratedModel):
    burn_time: int | Annotated[str, IdSpec(registry='context_int_provider')] | KnownContextIntProviderId
    speed_multiplier: float | Annotated[str, IdSpec(registry='context_float_provider')] | KnownContextFloatProviderId
