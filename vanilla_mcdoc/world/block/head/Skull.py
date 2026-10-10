"""
Generated from symbols.json for ::java::world::block::head::Skull
Local link to file: vanilla_mcdoc/world/block/head/Skull.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from vanilla_mcdoc.util.avatar.Profile import Profile
    from vanilla_mcdoc.util.text.Text import Text


class Skull(BlockEntity):
    ExtraType: str | None = None  # Name of the owner, if exists will be converted to SkullOwner.
    note_block_sound: Annotated[str, IdSpec(registry='weighed_sound_event')] | None = None  # Sound to play when played with a note block. Only works on player head.
    profile: Profile | None = None  # Only works on player head.
    custom_name: Text | None = None
