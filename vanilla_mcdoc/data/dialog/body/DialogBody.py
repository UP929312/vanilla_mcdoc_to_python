"""
Generated from symbols.json for ::java::data::dialog::body::DialogBody
Local link to file: vanilla_mcdoc/data/dialog/body/DialogBody.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.data.dialog.body.ItemBody import ItemBody
from vanilla_mcdoc.data.dialog.body.PlainMessage import PlainMessage


class DialogBodyItem(ItemBody):
    type: Literal['minecraft:item', 'item'] = 'minecraft:item'


class DialogBodyPlainMessage(PlainMessage):
    type: Literal['minecraft:plain_message', 'plain_message'] = 'minecraft:plain_message'


type DialogBody = Annotated[
    DialogBodyItem | DialogBodyPlainMessage,
    Field(discriminator='type'),
]
