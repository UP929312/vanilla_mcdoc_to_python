"""
Generated from symbols.json for ::java::data::slot_source::SlotSource
Local link to file: vanilla_mcdoc/data/slot_source/SlotSource.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.slot_source.TypedSlotSource import TypedSlotSource
    from vanilla_mcdoc.registry.KnownSlotSourceId import KnownSlotSourceId


type SlotSource = TypedSlotSource | list[SlotSource] | Annotated[str, IdSpec(registry='slot_source', tags='allowed')] | KnownSlotSourceId
