"""
Generated from symbols.json for ::java::data::dialog::input::InputControl
Local link to file: vanilla_mcdoc/data/dialog/input/InputControl.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.data.dialog.input.BooleanInput import BooleanInput
from vanilla_mcdoc.data.dialog.input.NumberRangeInput import NumberRangeInput
from vanilla_mcdoc.data.dialog.input.SingleOptionInput import SingleOptionInput
from vanilla_mcdoc.data.dialog.input.TextInput import TextInput


class InputControlBoolean(BooleanInput):
    type: Literal['minecraft:boolean', 'boolean'] = 'minecraft:boolean'
    key: Annotated[str, Field(min_length=1), Field(pattern='^[A-Za-z0-9_]*$')] | str  # The input key, which is used to build macro command and generate custom action payload.


class InputControlNumberRange(NumberRangeInput):
    type: Literal['minecraft:number_range', 'number_range'] = 'minecraft:number_range'
    key: Annotated[str, Field(min_length=1), Field(pattern='^[A-Za-z0-9_]*$')] | str  # The input key, which is used to build macro command and generate custom action payload.


class InputControlSingleOption(SingleOptionInput):
    type: Literal['minecraft:single_option', 'single_option'] = 'minecraft:single_option'
    key: Annotated[str, Field(min_length=1), Field(pattern='^[A-Za-z0-9_]*$')] | str  # The input key, which is used to build macro command and generate custom action payload.


class InputControlText(TextInput):
    type: Literal['minecraft:text', 'text'] = 'minecraft:text'
    key: Annotated[str, Field(min_length=1), Field(pattern='^[A-Za-z0-9_]*$')] | str  # The input key, which is used to build macro command and generate custom action payload.


type InputControl = Annotated[
    InputControlBoolean | InputControlNumberRange | InputControlSingleOption | InputControlText,
    Field(discriminator='type'),
]
