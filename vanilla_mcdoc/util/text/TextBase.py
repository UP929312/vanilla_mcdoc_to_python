"""
Generated from symbols.json for ::java::util::text::TextBase
Local link to file: vanilla_mcdoc/util/text/TextBase.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.util.text.TextStyle import TextStyle

if TYPE_CHECKING:
    from vanilla_mcdoc.util.text.Text import Text


class TextBase(TextStyle):
    extra: Annotated[list[Text], Field(min_length=1)] | None = None
