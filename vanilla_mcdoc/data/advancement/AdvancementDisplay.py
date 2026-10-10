"""
Generated from symbols.json for ::java::data::advancement::AdvancementDisplay
Local link to file: vanilla_mcdoc/data/advancement/AdvancementDisplay.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.AdvancementFrame import AdvancementFrame
    from vanilla_mcdoc.util.text.Text import Text
    from vanilla_mcdoc.world.item.ItemStackTemplate import ItemStackTemplate


class AdvancementDisplay(GeneratedModel):
    icon: ItemStackTemplate
    title: Text
    description: Text
    frame: AdvancementFrame | None = None  # Controls the advancement tile frame. Defaults to `task`.
    show_toast: bool | None = None  # Whether to show the toast pop up after completing this advancement. Defaults to `true`.
    announce_to_chat: bool | None = None  # Whether to announce in the chat when this advancement has been completed. Defaults to `true`.
    hidden: bool | None = None  # Whether or not to hide this advancement and all its children from the advancement screen, until this advancement have been completed. Has no effect on root advancements themselves, but still affects all their children. Defaults to `false`.
