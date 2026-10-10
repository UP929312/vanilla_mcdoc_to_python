# ~~~ WHAT ARE WE TESTING ~~~

# Text's definition is cyclical - It can be str | list[<self>]

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::util::text::Text
Local link to file: vanilla_mcdoc/util/text/Text.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

if TYPE_CHECKING:
    from vanilla_mcdoc.util.text.TextObject import TextObject


type Text = str | TextObject | Annotated[list[Text], Field(min_length=1)]
