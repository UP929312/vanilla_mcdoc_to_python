# ~~~ WHAT ARE WE TESTING ~~~

# Text's definition is cyclical - It can be str | list[<self>]

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::util::text::Text
Local link to file: generated_symbols/util/text/Text.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.util.text.TextObject import TextObject


type Text = str | TextObject | Annotated[list[Text], 'Length = 1 (inclusive) and above']
