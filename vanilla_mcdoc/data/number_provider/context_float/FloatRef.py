"""
Generated from symbols.json for ::java::data::number_provider::context_float::FloatRef
Local link to file: vanilla_mcdoc/data/number_provider/context_float/FloatRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.context_float.ContextFloatProvider import ContextFloatProvider
    from vanilla_mcdoc.registry.KnownContextFloatProviderId import KnownContextFloatProviderId


type FloatRef = Annotated[str, IdSpec(registry='context_float_provider')] | KnownContextFloatProviderId | ContextFloatProvider
