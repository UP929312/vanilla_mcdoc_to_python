# ~~~ WHAT ARE WE TESTING ~~~

# Nothing in particular, just a nice, nested object with lots going on

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::data::advancement::AdvancementDisplay
Local link to file: generated_symbols/data/advancement/AdvancementDisplay.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.advancement.AdvancementFrame import AdvancementFrame
    from generated_symbols.util.text.Text import Text
    from generated_symbols.world.item.ItemStackTemplate import ItemStackTemplate


@dataclass(kw_only=True)
class AdvancementDisplay:
    icon: ItemStackTemplate
    title: Text
    description: Text
    background: Annotated[str, IdSpec(registry='texture')] | None = None  # Used for the advancement tab (root advancement only).
    frame: AdvancementFrame | None = None  # Controls the advancement tile frame. Defaults to `task`.
    show_toast: bool | None = None  # Whether to show the toast pop up after completing this advancement. Defaults to `true`.
    announce_to_chat: bool | None = None  # Whether to announce in the chat when this advancement has been completed. Defaults to `true`.
    hidden: bool | None = None  # Whether or not to hide this advancement and all its children from the advancement screen, until this advancement have been completed. Has no effect on root advancements themselves, but still affects all their children. Defaults to `false`.
