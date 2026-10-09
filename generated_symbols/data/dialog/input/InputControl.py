"""
Generated from symbols.json for ::java::data::dialog::input::InputControl
Local link to file: generated_symbols/data/dialog/input/InputControl.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from generated_symbols.data.dialog.input.BooleanInput import BooleanInput
from generated_symbols.data.dialog.input.NumberRangeInput import NumberRangeInput
from generated_symbols.data.dialog.input.SingleOptionInput import SingleOptionInput
from generated_symbols.data.dialog.input.TextInput import TextInput
from pydantic import Field


class InputControlBoolean(BooleanInput):
    type: Literal['minecraft:boolean', 'boolean'] = 'minecraft:boolean'
    key: Annotated[str, Field(min_length=1)] | str  # The input key, which is used to build macro command and generate custom action payload.


class InputControlNumberRange(NumberRangeInput):
    type: Literal['minecraft:number_range', 'number_range'] = 'minecraft:number_range'
    key: Annotated[str, Field(min_length=1)] | str  # The input key, which is used to build macro command and generate custom action payload.


class InputControlSingleOption(SingleOptionInput):
    type: Literal['minecraft:single_option', 'single_option'] = 'minecraft:single_option'
    key: Annotated[str, Field(min_length=1)] | str  # The input key, which is used to build macro command and generate custom action payload.


class InputControlText(TextInput):
    type: Literal['minecraft:text', 'text'] = 'minecraft:text'
    key: Annotated[str, Field(min_length=1)] | str  # The input key, which is used to build macro command and generate custom action payload.


type InputControl = Annotated[
    InputControlBoolean | InputControlNumberRange | InputControlSingleOption | InputControlText,
    Field(discriminator='type'),
]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::input::InputControl": {
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
                                    "value": "input_control_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "The input key, which is used to build macro command and generate custom action payload.",
                "key": "key",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "union",
                            "members": [
                                {
                                    "kind": "string",
                                    "lengthRange": {
                                        "kind": 0,
                                        "min": 1
                                    },
                                    "attributes": [
                                        {
                                            "name": "match_regex",
                                            "value": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "^[A-Za-z0-9_]*$"
                                                }
                                            }
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "kind": "dispatcher",
                            "parallelIndices": [
                                {
                                    "kind": "static",
                                    "value": "%fallback"
                                }
                            ],
                            "registry": "mcdoc:custom_dynamic_event_keys"
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
                    "registry": "minecraft:input_control"
                }
            }
        ]
    }
}

