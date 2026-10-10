"""
Generated from symbols.json for ::java::data::dialog::input::NumberRangeInput
Local link to file: vanilla_mcdoc/data/dialog/input/NumberRangeInput.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.text.Text import Text


class NumberRangeInput(GeneratedModel):
    width: Annotated[int, Field(ge=1, le=1024)] | None = None  # Defaults to 200.
    label: Text  # Label displayed on the slider.
    label_format: str | None = None  # The translation to be used for building label. `%1$s` is replaced by `label`; `%2$s` is replaced by current value of the slider. Defaults to `options.generic_value`.
    start: float  # Start value, inclusive.
    end: float  # End value, inclusive.
    step: Annotated[float, Field(gt=0)] | None = None  # Step size of the input. If not present, any value from range is allowed.
    initial: float | None = None  # Initial value of the slider. Rounded down nearest step. Defaults to the middle of the range.
