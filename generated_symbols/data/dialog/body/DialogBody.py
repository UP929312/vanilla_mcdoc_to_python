"""
Generated from symbols.json for ::java::data::dialog::body::DialogBody
Local link to file: generated_symbols/data/dialog/body/DialogBody.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from generated_symbols.data.dialog.body.ItemBody import ItemBody
from generated_symbols.data.dialog.body.PlainMessage import PlainMessage


class DialogBodyItem(ItemBody):
    type: Literal['minecraft:item', 'item'] = 'minecraft:item'


class DialogBodyPlainMessage(PlainMessage):
    type: Literal['minecraft:plain_message', 'plain_message'] = 'minecraft:plain_message'


type DialogBody = Annotated[
    DialogBodyItem | DialogBodyPlainMessage,
    Field(discriminator='type'),
]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::body::DialogBody": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "dialog_body_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:dialog_body"
                }
            }
        ]
    }
}
