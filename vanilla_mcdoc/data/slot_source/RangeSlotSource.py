"""
Generated from symbols.json for ::java::data::slot_source::RangeSlotSource
Local link to file: vanilla_mcdoc/data/slot_source/RangeSlotSource.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar, Literal

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.BlockEntityTarget import BlockEntityTarget
    from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget


class RangeSlotSource(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'slot_source'

    source: EntityTarget | BlockEntityTarget | Literal['container'] | None = None  # Defaults to `container`.
    slots: str
