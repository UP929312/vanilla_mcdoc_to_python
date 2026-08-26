"""
Generated from symbols.json for ::java::data::dialog::body::DialogBody
Local link to file: generated_symbols/data/dialog/body/DialogBody.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

from generated_symbols.data.dialog.body.ItemBody import ItemBody
from generated_symbols.data.dialog.body.PlainMessage import PlainMessage


@dataclass(kw_only=True)
class DialogBodyItem(ItemBody):
    type: Literal['minecraft:item']


@dataclass(kw_only=True)
class DialogBodyPlainMessage(PlainMessage):
    type: Literal['minecraft:plain_message']


type DialogBody = DialogBodyItem | DialogBodyPlainMessage


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

