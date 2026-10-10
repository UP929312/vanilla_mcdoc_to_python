"""
Generated from symbols.json for ::java::data::dialog::DialogListRef
Local link to file: vanilla_mcdoc/data/dialog/DialogListRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.dialog.Dialog import Dialog
    from vanilla_mcdoc.registry.KnownDialogId import KnownDialogId


type DialogListRef = Dialog | Annotated[str, IdSpec(registry='dialog', tags='allowed')] | KnownDialogId | list[Annotated[str, IdSpec(registry='dialog')] | KnownDialogId | Dialog]
