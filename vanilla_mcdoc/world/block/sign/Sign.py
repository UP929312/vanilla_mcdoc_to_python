"""
Generated from symbols.json for ::java::world::block::sign::Sign
Local link to file: vanilla_mcdoc/world/block/sign/Sign.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.block.SignText import SignText


class Sign(BlockEntity):
    back_text: SignText | None = None
    front_text: SignText | None = None
    is_waxed: bool | None = None  # Whether the sign has been made uneditable by applying wax.
    allow_op_features: bool | None = None  # Whether the sign allows following features: 1. Resolving text components 2. Executing click events  Defaults to `false`.
