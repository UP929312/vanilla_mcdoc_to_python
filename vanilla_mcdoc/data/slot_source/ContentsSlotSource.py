"""
Generated from symbols.json for ::java::data::slot_source::ContentsSlotSource
Local link to file: vanilla_mcdoc/data/slot_source/ContentsSlotSource.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.function.ContainerComponents import ContainerComponents
    from vanilla_mcdoc.data.slot_source.SlotSource import SlotSource


class ContentsSlotSource(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'slot_source'

    slot_source: SlotSource  # The slots to search.
    component: ContainerComponents  # If an item targeted by `slot_source` has this container component, selects all items inside.
